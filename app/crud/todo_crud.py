from flask import request

from app.models.models import User, Todo, todo_schema, todos_schema
from app.helpers import validators, helpers
from app.helpers.extensions import db
from app.helpers.responses import fail_response, success_response

def create_todo_for_user(todo: Todo):
    """Creates a todo for current active user"""

    user_email = helpers.get_email_from_token()
    user = User.query.filter(User.email == user_email).first()
    if user is None:
        return fail_response.user_not_found(user_email)
    
    validators.check_todo_content_is_valid(todo['content'])
    validators.check_todo_priority_is_valid(todo['priority'])

    new_todo = todo_schema.load(todo, session=db.session)
    user.todos.append(new_todo)
    db.session.commit()

    return todo_schema.dump(new_todo), 201

def read_one_todo(todo_id: int):
    """Reads one todo, selected by id"""
    user_email = helpers.get_email_from_token()

    todo = Todo.query.filter(Todo.user_email == user_email, Todo.id == todo_id).first()
    if todo:
        return todo_schema.dump(todo), 200
    else:
        return fail_response.todo_not_found(todo_id)

def read_user_todos(priority: int=None):
    "Reads all user todos, option to filter by priority"
    user_email = helpers.get_email_from_token()

    if priority:
        validators.check_todo_priority_is_valid(priority)
        todos = Todo.query.filter(Todo.user_email == user_email, Todo.priority >= priority).all()
    else:
        todos = Todo.query.filter(Todo.user_email == user_email).all()
    
    return todos_schema.dump(todos), 200

def update_todo(todo_id: int):
    "Updates todo info"
    user_email = helpers.get_email_from_token()

    todo = Todo.query.filter(Todo.user_email == user_email, Todo.id == todo_id).first()
    if todo is None:
        return fail_response.todo_not_found(todo_id)
    
    todo_data = request.get_json()
    content = todo_data.get('content', None)
    priority = todo_data.get('priority', None)

    if content is None and priority is None:
        return fail_response.missing_content_and_priority()
    elif content and priority:
        validators.check_todo_content_is_valid(content)
        validators.check_todo_priority_is_valid(priority)
        todo.content = content
        todo.priority = priority
    elif content:
        validators.check_todo_content_is_valid(content)
        todo.content = content
    else:
        validators.check_todo_priority_is_valid(priority)
        todo.priority = priority

    db.session.merge(todo)
    db.session.commit()
    return todo_schema.dump(todo), 200

def delete_todo(todo_id: int):
    "Deletes todo selected by id"
    user_email = helpers.get_email_from_token()

    todo = Todo.query.filter(Todo.user_email == user_email, Todo.id == todo_id).first()
    if todo is None:
        return fail_response.todo_not_found(todo_id)
    
    db.session.delete(todo)
    db.session.commit()
    return success_response.todo_deleted(todo_id)



