from flask import Blueprint

students_bp = Blueprint(
    "students",
    __name__,
    template_folder="templates"
)

from . import route