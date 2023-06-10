from flask import make_response

# 200 Success responses
def user_deleted(email):
    return make_response(
        f"User with email {email} successfully deleted", 200
    )

def todo_deleted(todo_id):
    return make_response(
        f"Todo with id {todo_id} successfully deleted", 200
    )