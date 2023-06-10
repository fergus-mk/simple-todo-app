from flask import jsonify, request

from app.auth.auth import login, token_required
from app.crud import user_crud, todo_crud


def init_user_routes(app):
    """User routes"""

    @app.route('/api/users', methods=['POST'])
    def post_user():
        """Create new user"""
        user = request.get_json()
        new_user, status = user_crud.create_user(user)
        
        return jsonify(new_user), status

    @token_required
    @app.route('/api/users', methods=['GET'])
    def get_user():
        """Reads current user"""
        return user_crud.get_user()
    
    @token_required
    @app.route('/api/users', methods=['PATCH'])
    def update_user():
        """Updates the first name and/or last name of a user"""
        return user_crud.update_user()

    @token_required
    @app.route('/api/users', methods=['DELETE'])
    def delete_user():
        """Deletes user"""
        return user_crud.delete_user()

def init_auth_routes(app):
    """Auth routes"""

    @app.route('/api/login', methods=['POST'])
    def login_route():
        """Log in and get login token"""
        return login() 

def init_todo_routes(app):
    """Todo routes"""

    @token_required
    @app.route('/api/todos', methods=['POST'])
    def create_todo():
        "Create new todo"
        todo = request.get_json()
        return todo_crud.create_todo_for_user(todo) 
    
    @token_required
    @app.route('/api/todos/<int:todo_id>', methods=['GET'])
    def read_todo(todo_id):
        """Get todo selected by id"""
        return todo_crud.read_one_todo(todo_id)

    @token_required
    @app.route('/api/todos', defaults={'priority': None}, methods=['GET'])
    @app.route('/api/todos/priority/<int:priority>', methods=['GET'])
    def read_todos(priority):
        """Read user todos and (optionally) filter by priority"""
        return todo_crud.read_user_todos(priority)
    
    @token_required
    @app.route('/api/todos/<int:todo_id>', methods=['PATCH'])
    def update_todo(todo_id):
        """Update the content and/or priority of a todo"""
        return todo_crud.update_todo(todo_id)

    @token_required
    @app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        "Delete a todo"
        return todo_crud.delete_todo(todo_id)