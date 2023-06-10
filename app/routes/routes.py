from flask import jsonify, request

from app.crud import user_crud, todo_crud
from app.auth.auth import login, token_required


def init_user_routes(app):

    @app.route('/api/user', methods=['POST'])
    def post_user():
        user = request.get_json()
        new_user, status = user_crud.create_user(user)
        
        return jsonify(new_user), status

    @token_required
    @app.route('/api/user', methods=['GET'])
    def get_user():
        """Reads current user"""
        return user_crud.get_user()
    
    @token_required
    @app.route('/api/user', methods=['PATCH'])
    def update_user():
        return user_crud.update_user()

    @token_required
    @app.route('/api/user', methods=['DELETE'])
    def delete_user():
        return user_crud.delete_user()

def init_auth_routes(app):

    @app.route('/api/login', methods=['POST'])
    def login_route():
        return login() 

def init_todo_routes(app):

    @token_required
    @app.route('/api/todo', methods=['POST'])
    def create_todo():
        todo = request.get_json()
        return todo_crud.create_todo_for_user(todo) 
    
    @token_required
    @app.route('/api/todo/<int:todo_id>', methods=['GET'])
    def read_todo(todo_id):
        return todo_crud.read_one_todo(todo_id)

    @token_required
    @app.route('/api/todos', defaults={'priority': None}, methods=['GET'])
    @app.route('/api/todos/<int:priority>', methods=['GET'])
    def read_todos(priority):
        return todo_crud.read_user_todos(priority)
    
    @token_required
    @app.route('/api/todo/<int:todo_id>', methods=['PATCH'])
    def update_todo(todo_id):
        return todo_crud.update_todo(todo_id)

    @token_required
    @app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        return todo_crud.delete_todo(todo_id)