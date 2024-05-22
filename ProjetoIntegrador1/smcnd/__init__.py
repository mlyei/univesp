from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def  create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/nome_do_banco_de_dados'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta'

    db.init_app(app)

    return app