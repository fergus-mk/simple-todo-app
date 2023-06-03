import os
from flask import Flask
from flask_migrate import Migrate

from app.routes.routes import init_routes
from app.extensions.extensions import db, ma
from app.models.models import User, Todo
from app.config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 

    db.init_app(app) 
    ma.init_app(app) 
    migrate = Migrate(app, db) 

    with app.app_context():     
        db.create_all()

    init_routes(app)

    return app
