from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, template_folder='templates/dashboard')

@bp.route('/dashboard')
def dashboard_home():
    return render_template('dashboard.html')