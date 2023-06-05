import bcrypt

from app.models.models import User, user_schema
from app.responses.fail_response import user_not_found, user_already_exists
from app.helpers import validators, helpers
from app.extensions.extensions import db

# def get_user(email):
#     """Uses email to get user from db"""
#     user = User.query.filter(User.email == email).first()

#     if user:
#             return user_schema.dump(user)
#     else:
#         return user_not_found(email)

def get_user():
    return helpers.get_email_from_token()

def create_user(user: User):
    "Takes User object and uses it to create user in user table, assigns a unique id"
    email = user.get("email")
    password = user.get("password").encode('utf-8')  # NEW


    validators.check_email_is_valid(email)
    validators.check_name_is_valid(user.get("first_name"))
    validators.check_name_is_valid(user.get("last_name"))
    validators.check_password_is_valid(user.get("password"))

    existing_user = User.query.filter(User.email == email).first()
    if existing_user:
        return user_already_exists(email)
    else:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt) # NEW
        user["password"] = hashed_password.decode('utf-8')  # NEW

        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    