# from flask_sqlalchemy import SQLAlchemy # REMOVED
# from flask_marshmallow import Marshmallow # REMOVED
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.extensions.extensions import db, ma


class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, db.ForeignKey("user.email"))
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False, default=1)


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True
        sqla_Session = db.session
        include_fk = True  # Also need this so marshmallow recognises person_id during serialization
    user_email = fields.Str()
    content = fields.Str()
    priority = fields.Integer()


class User(db.Model):
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


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_Session = db.session
        include_relationships = True  # This means it will also go into neighbouring schema

    email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    todos = fields.Nested(TodoSchema, many=True)


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
user_schema = UserSchema()