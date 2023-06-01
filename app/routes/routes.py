from flask import jsonify

from app.models.test_ma_model import user_schema

def init_routes(app):

    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "todos api up and running",
            "success": True,
            "data": None
        }), 200
    
    @app.route("/api/test_marshmallow", methods=["GET"])
    def test_marshmallow():
        # Test marshmallow by serializing some data
        user = {"name": "Fergus Dergus", "email": "john@example.com"}
        return user_schema.dump(user), 200