from app import create_app
from datetime import timedelta

app = create_app()

app.config["SECRET_KEY"] = "dev"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)

if __name__ == "__main__":
    app.run(debug=True)