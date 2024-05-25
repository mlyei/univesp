from flask import Blueprint

bp = Blueprint('escola', __name__)

from smcnd.escola import routes