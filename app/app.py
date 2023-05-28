from flask_migrate import Migrate
from create_app import create_app

# load_dotenv()

app = create_app()
# ma = create_ma(app) # REMOVED

# db.init_app(app)
# migrate = Migrate(app, db)

print("Flask app is running!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)