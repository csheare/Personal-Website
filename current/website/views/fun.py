from flask import render_template, Blueprint
bp  = Blueprint('fun', __name__)

@bp.route("/fun", methods=['GET'])
def basic():
    return render_template('fun/fun.html')
