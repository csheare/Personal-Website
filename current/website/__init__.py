from flask import Flask,current_app,render_template,g,request,redirect,url_for,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from website.views import business,fun,home
import sqlite3, os
from website.db import db
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
import json
from website.models import WebSite


def create_app():

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    jwt = JWTManager(app)

    @app.route('/')
    def base():
        return render_template('base.html')

    @jwt.expired_token_loader
    def lame(expired_token):
        return jsonify({"expired_token" : expired_token})

    # With JWT_COOKIE_CSRF_PROTECT set to True, set_access_cookies() and
    # set_refresh_cookies() will now also set the non-httponly CSRF cookies
    # as well
    @app.route('/token/auth', methods=['POST'])
    def login():
        print("Logging in...")
        result = request.form.to_dict()
        data = WebSite.check_password(result['Password'])

        # Create the tokens we will be sending back to the user
        access_token = create_access_token(identity=data.make_json())
        refresh_token = create_refresh_token(identity=data.make_json())

        # Set the JWTs and the CSRF double submit protection cookies
        # in this response
        resp = make_response(redirect("/api/{}".format(data.route)))
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        print(access_token)
        return resp


    @app.route('/token/refresh', methods=['POST'])
    @jwt_refresh_token_required
    def refresh():
        print("Refreshing...")
        # Create the new access token
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)

        # Set the access JWT and CSRF double submit protection cookies
        # in this response
        resp = jsonify({'refresh': True})
        set_access_cookies(resp, access_token)
        return redirect("/api/example")


    # Because the JWTs are stored in an httponly cookie now, we cannot
    # log the user out by simply deleting the cookie in the frontend.
    # We need the backend to send us a response to delete the cookies
    # in order to logout. unset_jwt_cookies is a helper function to
    # do just that.
    @app.route('/token/remove', methods=['POST'])
    def logout():
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        print("logging out")
        return resp, 200

    @app.route('/api/gouda', methods=['GET'])
    @jwt_required
    def protected():
       return render_template('welcome.html')

    # register blueprints
    app.register_blueprint(business.bp)
    app.register_blueprint(fun.bp)
    app.register_blueprint(home.bp)

    return app
