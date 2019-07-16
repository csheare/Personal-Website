from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from website.views import business,fun,home


def create_app():

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')
    
    @app.route('/')
    def base():
        return render_template('base.html')

    # register blueprints
    app.register_blueprint(business.bp)
    app.register_blueprint(fun.bp)
    app.register_blueprint(home.bp)

    return app
