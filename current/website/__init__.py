from flask import Flask,render_template
from website.views import business,fun,home

# Now we can access the configuration variables via app.config["VAR_NAME"].

# application factory function
def create_app():
    # creates the Flask instance
    # __name__ is the name of the current Python module
    # instance_relative_config tells the app the config file is in the instance folder
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return render_template('base.html')

# register blueprints
    app.register_blueprint(business.bp)
    app.register_blueprint(fun.bp)
    app.register_blueprint(home.bp)

    return app

