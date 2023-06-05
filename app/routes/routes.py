from flask import jsonify, request # ADDED request

from app.models.test_ma_model import user_schema
from app.responses.fail_response import user_not_provided
from app.crud import user_crud
from app.auth.auth import login, token_required

def init_routes(app):

    
    @app.route("/api/test_marshmallow", methods=["GET"])
    def test_marshmallow():
        # Test marshmallow by serializing some data
        user = {"name": "Fergus Dergus", "email": "john@example.com"}
        return user_schema.dump(user), 200
    
    # @app.route('/user/<email>')
    # def read_one_user(email: str):
    #     """Reads one user, selected by email"""
    #     return user_crud.get_user(email)
    
    # @token_required
    # @app.route('/api/user/get_user')
    # def get_user_route():
    #     return user_crud.get_user()

    @token_required
    @app.route('/api/user/get_user')
    def get_user_route():
        """Reads one user, selected by email"""
        return user_crud.get_user()

    
    @app.route('/user', methods=['POST']) # ADDED - UNSURE ABOUT THIS
    def post_user():
        user = request.get_json()
        if not user:
            return user_not_provided   # THIS ISN't working - already error from no JSON
        try:
            new_user, status = user_crud.create_user(user)
            return jsonify(new_user), status
        except Exception as e:
            return jsonify({"message": str(e)}), 400
        
    # Auth
    @app.route('/login', methods=['POST'])
    def login_route():
        return login() 