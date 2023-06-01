import os
from dotenv import load_dotenv

class Config(object):
    load_dotenv()  # take environment variables from .env.

    
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


print(f"Secret key: {Config.SECRET_KEY}")
print(f"DB URI: {Config.SQLALCHEMY_DATABASE_URI}")