# app/create_app.py
import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.models.models import db
from app.routes.routes import init_routes
from app.extensions.extensions import ma  # NEW

def create_app():
    app = Flask(__name__)
    load_dotenv()  # take environment variables from .env.

    secret_key = os.getenv("SECRET_KEY")
    if secret_key is None:
        raise ValueError("No SECRET_KEY set for Flask application")

    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    if db_uri is None:
        raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application")

    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    db.init_app(app)

    init_routes(app)

    return app

def create_ma(app):
    # ma = Marshmallow(app) # REMOVED
    ma.init_app(app) # NEW
    return ma