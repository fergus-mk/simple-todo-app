from flask import abort

# 400 Bad Request errors
def email_not_valid(error):
    abort(
        400,
        f"Email is not valid: {error}"
    )

def name_not_alpha():
    abort(
        400,
        f"Name contains non-alphabetical characters"
    )

def user_not_provided():
    abort(
        400,
        f"User not provided"
    )

def password_not_valid():
    abort(
        400,
        f"Password must be at least 5 characters long and contain at least one digit and special character"
    )

def wrong_len_response(choice: str, type_describe: str):
    if choice=="short":
        abort(
            400,
            f"{type_describe} is too short, it must be at least 2 characters"
        )
    elif choice=="long":
        abort(
            400,
            f"{type_describe} is too long, it cannot be more than 50 characters"
        )

def missing_user_fields_error():
    abort(
        400,
        f"Missing required field(s) in user data must contain email, first name, last name and password "
    )

def missing_names():
    abort(
        400,
        "Please provide fist name and/or last name"
    )

def missing_content_and_priority():
    abort(
        400,
        "Please provide content and/or priority"
    )

def priority_out_of_range():
        abort(
            400,
            "Priority must be from 0-5"
        )

# 401 Unauthorized errors
def invalid_username_or_password():
    abort(
        401,
        f"Invalid username or password"
    )

def token_not_found():
    abort(
        401,
        f"Token not found"
    )

# 404 Not Found errors
def todo_not_found(id):
    abort(
        404,
        f"Todo with id: {id} not found"
    )

def user_not_found(email):
    abort(
        404, 
        f"User with email {email} not found"
    )

# 409 Conflict errors
def user_already_exists(email):
    abort(
        409,
        f"User with email: {email} already exists"
    )
