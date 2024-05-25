from flask import Blueprint

bp = Blueprint('main', __name__)

from smcnd.main import routes