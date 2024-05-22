import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_key"
    SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@ip/nomedabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False