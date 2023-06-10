from flask import make_response


def user_deleted(email):
    return make_response(
        f"User with email {email} sucessfully deleted", 200
    )

def todo_deleted(todo_id):
    return make_response(
        f"Todo with id {todo_id} sucessfully deleted", 200
    )