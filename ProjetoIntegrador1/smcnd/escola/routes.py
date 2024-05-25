from flask import Blueprint, render_template

bp = Blueprint('escola', __name__,)

@bp.route('/escola')
def escola_home():
    return render_template('escola.html')
