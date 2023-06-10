from marshmallow import fields

from app.helpers.extensions import db, ma


class Todo(db.Model):
    """Todo table containing todo items for users"""
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey("user.email"))
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=1)


class TodoSchema(ma.SQLAlchemyAutoSchema):
    """TodoSchema for serializing and deserializing Todo instances"""
    class Meta:
        model = Todo
        load_instance = True  # Deserialize to model instance
        sqla_Session = db.session
        include_fk = True  # So marshmallow recognises person_id during serialization
    user_email = fields.Str()
    content = fields.Str()
    priority = fields.Integer()


class User(db.Model):
    """User table containing user details"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String, nullable=False)

    todos = db.relationship(
        Todo,
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )

    def __repr__(self):
        return f"User {self.first_name} {self.last_name} with email {self.email}"


class UserLoadSchema(ma.SQLAlchemyAutoSchema):
    """UserLoadSchema for deserializing User instances"""
    class Meta:
        model = User
        load_instance = True
        sqla_Session = db.session
        include_relationships = True  # This means it will also go into neighbouring schema
        exclude = ("id", "password")  # Exclude password and id during deserialization

    email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    password = fields.Str() # Password needed for user load
    todos = fields.Nested(TodoSchema, many=True)


class UserDumpSchema(ma.SQLAlchemyAutoSchema):
    """UserDumpSchema for serializing User instances"""
    class Meta:
        model = User
        load_instance = True   # Deserialize to model instance
        sqla_Session = db.session
        include_relationships = True
        exclude = ("id", "password")

    email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    todos = fields.Nested(TodoSchema, many=True)

# Initialized schemas for global use throughout the app
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)  # Many=True to serialize a list of objects
user_load_schema = UserLoadSchema()  # Used for deserializing user data from requests
user_dump_schema = UserDumpSchema()  # Used for serializing user data to responses