from flask import Blueprint, render_template


bp = Blueprint('main', __name__)

@bp.routes('/')

def index():
    return render_template('index.html')