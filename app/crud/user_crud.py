import bcrypt
from flask import request

from app.models.models import User, user_load_schema, user_dump_schema # HERE
from app.helpers import validators, helpers
from app.helpers.extensions import db
from app.helpers.responses import fail_response, success_response


# def create_user(user: User):
#     "Takes User object and uses it to create user in user table, assigns a unique id"
#     validators.check_all_fields(user)

#     email = user.get("email")
#     password = user.get("password").encode('utf-8')

#     validators.check_email_is_valid(email)
#     validators.check_name_is_valid(user.get("first_name"))
#     validators.check_name_is_valid(user.get("last_name"))
#     validators.check_password_is_valid(user.get("password"))

#     existing_user = User.query.filter(User.email == email).first()
#     if existing_user:
#         return fail_response.user_already_exists(email)
#     else:
#         salt = bcrypt.gensalt()
#         hashed_password = bcrypt.hashpw(password, salt)
#         user["password"] = hashed_password.decode('utf-8')

#         print("LOOK HERE!!!!!!!!!!!!!!!!!!!!!")
#         print(user)  # Add this line to debug

#         new_user = user_load_schema.load(user, session=db.session)
#         db.session.add(new_user)
#         db.session.commit()
#         return user_dump_schema.dump(new_user), 201

def create_user(user: User):
    # ...
    email = user.get("email")
    password = user.get("password").encode('utf-8')

    validators.check_email_is_valid(email)
    validators.check_name_is_valid(user.get("first_name"))
    validators.check_name_is_valid(user.get("last_name"))
    validators.check_password_is_valid(user.get("password"))

    existing_user = User.query.filter(User.email == email).first()
    if existing_user:
        return fail_response.user_already_exists(email)
    else:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        user["password"] = hashed_password.decode('utf-8')

        # Manually handle the password field
        password = user.pop("password")
        new_user = user_load_schema.load(user, session=db.session)
        new_user.password = password

        db.session.add(new_user)
        db.session.commit()
        return user_dump_schema.dump(new_user), 201

def get_user():
    "Reads current user"
    user_email = helpers.get_email_from_token()
    user = User.query.filter(User.email == user_email).first()

    if user:
            return user_dump_schema.dump(user)
    else:
        return fail_response.user_not_found(user_email)

def update_user():
    "Updates user info"
    user_email = helpers.get_email_from_token()
    user = User.query.filter(User.email == user_email).first()
    if user is None:
        return fail_response.user_not_found(user_email)

    user_data = request.get_json()
    first_name = user_data.get('first_name', None)
    last_name = user_data.get('last_name', None)

    if first_name is None and last_name is None:
        return fail_response.missing_names()
    elif first_name and last_name:
        validators.check_name_is_valid(first_name)
        validators.check_name_is_valid(last_name)
        user.first_name = first_name
        user.last_name = last_name
    elif first_name:
        validators.check_name_is_valid(first_name)
        user.first_name = first_name
    else:
        validators.check_name_is_valid(last_name)
        user.last_name = last_name

    db.session.merge(user)
    db.session.commit()
    return user_dump_schema.dump(user), 200

def delete_user():
    """Deletes current user"""
    user_email = helpers.get_email_from_token()
    existing_user = User.query.filter(User.email == user_email).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return success_response.user_deleted(user_email)
    else:
        return fail_response.user_not_found(user_email)