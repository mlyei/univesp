from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.auth('/signin')
def signin():
    return render_template('signin.html')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@bp.route('/alunos')
def alunos():
    return render_template('alunos.html')

@bp.route('/escolas')
def escolas():
    return render_template('escolas.html')