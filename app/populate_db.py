from app import create_app, db
from models.models import User

app = create_app()

with app.app_context():
    # Create five example users
    users_data = [
        {
            'email': 'John@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        },
        {
            'email': 'Jane@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith'
        },
        {
            'email': 'Alice@example.com',
            'first_name': 'Alice',
            'last_name': 'Johnson'
        },
        {
            'email': 'Bob@example.com',
            'first_name': 'Bob',
            'last_name': 'Williams'
        },
        {
            'email': 'Emily@example.com',
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