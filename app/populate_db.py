from app import create_app, db
from models.models import User

app = create_app()
app.app_context().push()  # Push the app context to ensure correct app binding

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

with app.app_context():
    # Create five example users
    users_data = [
        {
            'email': 'user1@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        },
        {
            'email': 'user2@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith'
        },
        {
            'email': 'user3@example.com',
            'first_name': 'Alice',
            'last_name': 'Johnson'
        },
        {
            'email': 'user4@example.com',
            'first_name': 'Bob',
            'last_name': 'Williams'
        },
        {
            'email': 'user5@example.com',
            'first_name': 'Emily',
            'last_name': 'Brown'
        }
    ]

    # Add the users to the database
    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)

    # Commit the changes
    db.session.commit()

print("Users have been added to the database.")
