import os
from flask import Flask
from flask_migrate import Migrate
# from dotenv import load_dotenv # REMOVED

from app.routes.routes import init_routes
from app.extensions.extensions import db, ma
from app.models.models import User, Todo
from app.config.config import Config # here

def create_app():
    app = Flask(__name__)
    # load_dotenv()  # take environment variables from .env. # HERE

    # secret_key = os.getenv("SECRET_KEY")# HERE
    # if secret_key is None: # HERE
    #     raise ValueError("No SECRET_KEY set for Flask application") # HERE

    # db_uri = os.getenv("SQLALCHEMY_DATABASE_URI") # HERE
    # if db_uri is None: # HERE
    #     raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application") # HERE

    # app.config["SECRET_KEY"] = secret_key # REMOVED
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_uri  # REMOVED
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # reduce overhead  # REMOVED
    app.config.from_object(Config)  # new line here

    db.init_app(app) # Here
    ma.init_app(app) # Here
    migrate = Migrate(app, db) # new line here

    with app.app_context():  # new line here
        db.create_all()  # new line here

    init_routes(app)

    return app