from flask import render_template, request, redirect, url_for, flash, session
from . import auth_bp
from Data.db import users


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            flash("Connexion reussie !", "success")
            #return redirect(url_for("dashboard.index"))
            return "Connecté "
        else:
            flash("Identifiants invalides !", "danger")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Deconnecte avec succes", "info")
    #return redirect(url_for("auth.login"))
    return "Deconnecté "