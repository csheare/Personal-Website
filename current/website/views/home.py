from flask import render_template, Blueprint
bp  = Blueprint('home', __name__)

@bp.route("/home", methods=['GET'])
def basic():
    return render_template('home/home.html')
