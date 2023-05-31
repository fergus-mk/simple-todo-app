from dotenv import load_dotenv
from app.create_app import create_app, create_ma

app = create_app()
ma = create_ma(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8001)
