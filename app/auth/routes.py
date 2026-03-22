from flask import render_template, request, redirect, url_for, flash, session
from . import auth_bp
from Data.db import users


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            flash("Connexion reussie !", "success")
            return redirect(url_for("dashboard.index"))
        else:
            flash("Identifiants invalides !", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm  = request.form.get("confirm_password")

        if not username or not password:
            flash("Tous les champs sont obligatoires.", "danger")
        elif username in users:
            flash("Ce nom d'utilisateur existe déjà.", "danger")
        elif password != confirm:
            flash("Les mots de passe ne correspondent pas.", "danger")
        else:
            users[username] = password
            flash("Compte créé avec succès ! Connectez-vous.", "success")
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")



@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Deconnecte avec succes", "info")
    return redirect(url_for("auth.login"))