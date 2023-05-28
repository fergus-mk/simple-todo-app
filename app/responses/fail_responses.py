from flask import abort

def no_users_found_in_db():
    abort(
        404,
        f"No users found, user db is empty"
    )