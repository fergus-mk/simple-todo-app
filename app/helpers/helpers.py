from flask import request, jsonify
import jwt 

from app.models.models import User
from app.responses.fail_response import token_not_found
from app.config.config import Config


def get_email_from_token():
    config = Config()
    token = None

    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(" ")[1]

    # if not token:
    #     return token_not_found

    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
        email = payload["email"]
        return email
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError as e:
        return jsonify({"message": f"Invalid token: {str(e)}"}), 401
