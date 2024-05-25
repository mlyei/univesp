import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_key"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@192.168.1.4:3336/PlataformaAEE'
    SQLALCHEMY_TRACK_MODIFICATIONS = False