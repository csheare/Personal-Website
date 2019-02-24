from flask import render_template, Blueprint
bp  = Blueprint('business', __name__)

@bp.route("/business", methods=['GET'])
def basic():
    return render_template('business/business.html')
