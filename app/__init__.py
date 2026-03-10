<<<<<<< HEAD

=======  
from flask import Flask
from .auth.routes import auth_bp
from .courses.route import courses_bp
from .students.route import students_bp
from .dashboard.route import dashboard_bp
from .teachers.route import teachers_bp
def create_app():
    app = Flask(__name__)

    app.secret_key = "super_secret_key"
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(teachers_bp)
    app.register_blueprint(dashboard_bp)
    return app