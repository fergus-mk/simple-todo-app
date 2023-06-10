from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger

from app.config.config import Config
from app.helpers.extensions import db, ma
from app.models.models import User, Todo
from app.routes.routes import init_user_routes, init_todo_routes, init_auth_routes

def create_app():
    """Create app instance"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) # Initalize db with app
    ma.init_app(app) # Initalize marshamallow with app
    migrate = Migrate(app, db) # Migrate db with app

    Swagger(app) # Will be used to create OpenAPI documentation 

    with app.app_context():     
        db.create_all() # Create all db tables

    init_user_routes(app)
    init_todo_routes(app)
    init_auth_routes(app)

    return app
