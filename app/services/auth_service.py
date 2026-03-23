from functools import wraps
from flask import session, redirect, url_for, flash, render_template
from Data.db import users

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            if session.get("logged_in"):
                flash("Session expirée, reconnectez-vous", "warning")
            else:
                flash("Vous devez etre connecte", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Acces refuse", "danger")
            return redirect(url_for("dashboard.index"))
        return f(*args, **kwargs)
    return decorated_function

def login_service(username,password):
    if username in users and users[username]["password"] == password:
        session["user"] = username
        session["role"] = users[username]["role"]
        session["logged_in"] = True 
        session.permanent = True
        flash("Connexion reussie !", "success")
        return redirect(url_for("dashboard.index"))
    else:
        flash("Identifiants invalides !", "danger")
        return redirect(url_for("auth.login"))

def logout_service():
    session.pop("user", None)
    flash("Deconnecte avec succes", "info")
    return redirect(url_for("auth.login"))

from flask import session, redirect, url_for, flash
from Data.db import users

def register_service(username, password, role="user"):
    if username in users:
        flash("Utilisateur existe deja", "warning")
        return redirect(url_for("auth.register"))
    if len(password) < 4:
        flash("Mot de passe trop court", "danger")
        return redirect(url_for("auth.register"))
    users[username] = {
        "password": password,
        "role": role
    }
    flash("Compte cree avec succes, connectez-vous", "success")
    return redirect(url_for("auth.login"))