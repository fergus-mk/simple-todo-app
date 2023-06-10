from flask import abort

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

def invalid_username_or_password():
    abort(
        400,
        f"Invalid username or password"
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

def token_not_found(): # 401 is unauthorised - this needs changed 
    abort(
        401,
        f"Token not found"
    )

def todo_not_found(id):
    abort(
        401,
        f"Todo with id: {id} not found"
    )

def user_not_found(email):
    abort(
        404, 
        f"User with email {email} not found"
    )

def user_already_exists(email):
    abort(
        406,
        f"User with email: {email} already exists"
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

def priority_out_of_range():
        abort(
            400,
            "Priority must be from 0-5"
        )