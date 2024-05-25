from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    # Registrar blueprints
    from smcnd.main.routes import bp as main_blueprint
    from smcnd.auth.routes import bp as auth_blueprint
    from smcnd.dashboard.routes import bp as dashboard_blueprint 
    from smcnd.escola.routes import bp as escola_blueprint
    from smcnd.aluno.routes import bp as aluno_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(aluno_blueprint)
    app.register_blueprint(escola_blueprint)

    return app
