import os
from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger

from app.routes.routes import init_user_routes, init_todo_routes, init_auth_routes
from app.helpers.extensions import db, ma
from app.models.models import User, Todo
from app.config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 
    ma.init_app(app) 
    migrate = Migrate(app, db) 

    Swagger(app)

    with app.app_context():     
        db.create_all()

    init_user_routes(app)
    init_todo_routes(app)
    init_auth_routes(app)

    return app
