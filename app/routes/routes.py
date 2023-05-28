from flask import jsonify

def init_routes(app):

    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "todos api up and running",
            "success": True,
            "data": None
        }), 200