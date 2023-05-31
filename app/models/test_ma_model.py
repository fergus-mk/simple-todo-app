from app.extensions.extensions import ma

# Create a simple Marshmallow schema
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "email")

user_schema = UserSchema()