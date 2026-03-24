from app import create_app
from dotenv import load_dotenv
from config import Config

load_dotenv()

app = create_app()
app.config.from_object(Config)

if __name__ == "__main__":
    app.run(debug=True)