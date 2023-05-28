from flask import jsonify, Blueprint

# Create a Blueprint for the routes
user_bp = Blueprint('user_bp', __name__)

def init_routes(user_crud, app):
    @user_bp.route('/users/<email>', methods=['GET'])
    def get_user(email):
        user_data = user_crud.read_one_user(email)
        return user_data

    app.register_blueprint(user_bp)


    def init_routes(app):
        
        @app.register_blueprint(user_bp)

        # Test routes
        @app.route("/api", methods=["GET"])
        def get_api_base_url():
            return jsonify({
                "msg": "todos api up and running",
                "success": True,
                "data": None
            }), 200
        