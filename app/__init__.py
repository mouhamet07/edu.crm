<<<<<<< HEAD

=======  
from flask import Flask
from .auth.routes import auth_bp
from .courses.route import courses_bp
from .students.route import students_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = "super_secret_key"
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(students_bp)
    return app
>>>>>>> 28929c549f553a81db4837883b734ea404f27ffc
  