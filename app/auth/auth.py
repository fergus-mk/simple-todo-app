import datetime
import bcrypt
import jwt
from flask import request, jsonify, abort
from functools import wraps

from app.models.models import User
from app.responses.fail_response import invalid_username_or_password
from app.config.config import Config

config = Config()

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return invalid_username_or_password()

    user = User.query.filter(User.email == email).first()

    if user is None or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')): # CHANGED THE PASSWORD ACCESS
        return invalid_username_or_password()

    token = generate_token(email)
    return token

def generate_token(email, expiration_minutes=30):
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes),
    }

    token = jwt.encode(payload, config.SECRET_KEY, algorithm='HS256')
    return token  # Decode the bytes object to a string

def verify_token(token):
    token_bytes = token.encode()  # Convert string to bytes # ADDED
    try:
        payload = jwt.decode(token_bytes, config.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError as e:
        raise Exception(f"Invalid token: {str(e)}")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            current_user = verify_token(token)
        except Exception as e:
            return jsonify({"message": str(e)}), 401

        return f(*args, current_user=current_user, **kwargs)

    return decorated
