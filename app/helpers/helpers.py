from flask import request, jsonify
import jwt 

from app.config.config import Config


def get_email_from_token():
    """Extracts and returns the email from the Authorization header token"""
    config = Config()
    token = None

    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(" ")[1]

    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
        email = payload["email"]
        return email
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError as e:
        return jsonify({"message": f"Invalid token: {str(e)}"}), 401
