

#JUSTE POUR TESTER LE LOGIN POUR VOIR SI BLUEPRINT DE COURSES FONCTIONNE

from flask import Blueprint, session, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login")
def login():
    session["user"] = "admin"  
    return "Connecté "


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return "Déconnecté "