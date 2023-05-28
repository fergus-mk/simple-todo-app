import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from dotenv import load_dotenv

from routes.routes import init_routes
from models.models import db
from crud.user_crud import UserCrud

load_dotenv()

def create_app(test_config=None):

    # creates an application that is named after the name of the file
    app = Flask(__name__)

    secret_key = os.getenv("SECRET_KEY")
    if secret_key is None:
        raise ValueError("No SECRET_KEY set for Flask application")

    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    if db_uri is None:
        raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application")

    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    ma = Marshmallow(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    user_crud = UserCrud()

    # Initialize Routes
    init_routes(user_crud, app)

    print("THIS FUNCTION IS BEING CALLED")

    return app

