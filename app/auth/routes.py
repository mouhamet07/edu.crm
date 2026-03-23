from flask import render_template, request
from . import auth_bp
from Data.db import users
from app.services.auth_service import login_service ,logout_service,   register_service

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return login_service(username,password)
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    return logout_service()


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")
        return register_service(username, password, role)
    return render_template("auth/register.html")