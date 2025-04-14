from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app.db import execute

user_bp = Blueprint("user", __name__, url_prefix="/user")


# Profil uživatele
@user_bp.route("/")
def profile():
    """
    Pokud uživatel není přihlášen, vypíše se flash message.
    """
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))

    return render_template("user.html", username=session['user'])


# Změna hesla
@user_bp.route("/change_password", methods=["GET", "POST"])
def change_password():
    """
    Umožní uživateli změnit své heslo.
    """
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        new_password = request.form["new_password"]
        current_user = session['user']

        # Příkaz pro aktualizaci hesla uživatele
        command = "UPDATE users SET password = :password WHERE username = :username"
        execute(command, {"password": new_password, "username": current_user})

        flash("Vaše heslo bylo úspěšně změněno.", "success")
        return redirect(url_for("user.profile"))

    return render_template("change_password.html")
