from flask import jsonify, request # ADDED request
from flasgger import swag_from

from app.models.test_ma_model import user_schema
from app.responses.fail_response import user_not_provided
from app.crud import user_crud
from app.auth.auth import login, token_required

def init_routes(app):

    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        """
        Get API base URL
        ---
        responses:
          200:
            description: The API base URL was successfully retrieved.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    msg:
                      type: string
                      description: The status message.
                      example: todos api up and running
                    success:
                      type: boolean
                      description: Indicates whether the operation was successful.
                      example: true
                    data:
                      description: The retrieved data (none in this case).
        """
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
    @swag_from({
        'tags': ['User'],
        'description': 'Reads one user, selected by the email in the token',
        'security': [{'Bearer': []}],
        'responses': {
            '200': {
                'description': 'Returns the email of the user associated with the provided token',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'string'
                        }
                    }
                }
            },
            '401': {
                'description': 'Unauthorized, the token is either missing, invalid or expired',
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'properties': {
                                'message': {
                                    'type': 'string'
                                }
                            }
                        }
                    }
                }
            }
        }
    })
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
    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': 'true',
                'schema': {
                    'id': 'User',
                    'required': ['email', 'password'],
                    'properties': {
                        'email': {
                            'type': 'string',
                            'description': 'The email of the user'
                        },
                        'password': {
                            'type': 'string',
                            'description': 'The password of the user'
                        },
                    },
                },
            },
        ],
        'responses': {
            '200': {
                'description': 'Successful login',
                'examples': {
                    'application/json': {
                        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
                    }
                }
            },
            '401': {
                'description': 'Invalid username or password',
            }
        },
    })
    def login_route():
        return login() 