# from dotenv import load_dotenv # REMOVED
from flask_migrate import Migrate

from app import create_app #, create_ma # REMOVED
from app.models.models import User, Todo # ADDED

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8001)
