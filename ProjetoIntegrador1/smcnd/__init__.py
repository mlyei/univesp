from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ProjetoIntegrador1.config import Config

db = SQLAlchemy()

def  create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    #blueprints para as rotas
    #from main
    #from auth
    #from dashboard
    #from escolas
    #from alunos

    return app