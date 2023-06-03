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
