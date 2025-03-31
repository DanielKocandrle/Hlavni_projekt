from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.db import execute

# vytvoření přihlašovacího blueprintu
bp = Blueprint("auth", __name__, url_prefix="/auth")

# přihlášení
@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"
        result = execute(command, (username, password))

        if result:
            session['user'] = username  # uloží uživatele do session
            flash("Přihlášení úspěšné", "success")
            return redirect(url_for("user.profile"))
        else:
            flash("Špatné uživatelské jméno nebo heslo", "danger")

    return render_template("login.html")

# odhlášení
@bp.route("/logout")
def logout():
    session.pop('user', None)  # odstraní uživatele ze session
    flash("Úspěšně jste se odhlásili", "info")
    return redirect(url_for("index"))

# blueprint pro uživatelský profil
user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/")
def profile():
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))
    return render_template("user.html", username=session['user'])