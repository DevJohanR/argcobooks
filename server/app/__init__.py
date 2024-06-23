# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db
from .main import create_app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    CORS(app)
    
    with app.app_context():
       db.create_all()

    return app
