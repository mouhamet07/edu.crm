from flask import Flask
from .auth.routes import auth_bp
from .courses.route import courses_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = "super_secret_key"  
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)

    return app