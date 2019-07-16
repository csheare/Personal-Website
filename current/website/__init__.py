from flask import Flask,current_app,render_template,g
from flask_sqlalchemy import SQLAlchemy
from website.views import business,fun,home
import sqlite3

def create_app():

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')

    from . import db
    db.init_app(app)

    @app.route('/')
    def base():
        return render_template('base.html')

    # register blueprints
    app.register_blueprint(business.bp)
    app.register_blueprint(fun.bp)
    app.register_blueprint(home.bp)

    return app
