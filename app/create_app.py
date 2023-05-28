import os
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow

from routes.routes import init_routes



def create_app(test_config=None):

    # creates an application that is named after the name of the file
    app = Flask(__name__)

    secret_key = os.getenv("SECRET_KEY")
    if secret_key is None:
        raise ValueError("No SECRET_KEY set for Flask application")

    db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
    if db_uri is None:
        raise ValueError("No SQLALCHEMY_DATABASE_URI set for Flask application")

    # app.config["SECRET_KEY"] = "some_dev_key" #Here
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usr:pwd@pgsql:5432/todos" #Here
    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    # Initialize Routes
    init_routes(app)

    print("THIS FUNCTION IS BEING CALLED")

    return app

def create_ma(app):
    ma = Marshmallow(app)
    return ma