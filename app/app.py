from flask_migrate import Migrate
from dotenv import load_dotenv

from create_app import create_app, create_ma
from models.models import db

load_dotenv()

app = create_app()
ma = create_ma(app)

db.init_app(app)
migrate = Migrate(app, db)

print("Flask app is running!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)