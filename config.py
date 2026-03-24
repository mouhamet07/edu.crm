import os
from datetime import timedelta
class Config:
    FLASK_APP = os.getenv('FLASK_APP', 'run.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True')
    APP_NAME = os.getenv('APP_NAME', 'MyFlaskApp')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    PERMANENT_SESSION_LIFETIME = timedelta(
        minutes=int(os.getenv("PERMANENT_SESSION_LIFETIME", 60))
    )