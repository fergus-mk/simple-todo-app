from app import app
from models import Todo, db

with app.app_context():
    for i in range(1, 6):
        todo = Todo(description=f"Sample Task {i}")
        db.session.add(todo)
    db.session.commit()
    print("Successfully populated the Todo table with 5 sample entries!")
