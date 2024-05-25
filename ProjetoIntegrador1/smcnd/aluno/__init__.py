from flask import Blueprint

bp = Blueprint('aluno', __name__)

from smcnd.aluno import routes