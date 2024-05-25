from flask import Blueprint

bp = Blueprint('dashboard', __name__)

from smcnd.dashboard import routes