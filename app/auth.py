from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.db import execute

# vytvoření přihlašovacího blueprintu
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=("GET", "POST"))
def login():
    """
    přihlášení pomoci dat z databaze
    """
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"
        role = "SELECT role FROM users WHERE username = ?"
        result = execute(command, (username, password))
        res2 = execute(role, (username,))

        if result:
            session['user'] = username  # uloží uživatele do session
            session['role'] = res2[0][0]
            flash("Přihlášení úspěšné", "success")
            return redirect(url_for("user.profile"))
        else:
            flash("Špatné uživatelské jméno nebo heslo", "danger")

    return render_template("login.html")

@bp.route("/logout")
def logout():
    """
    odhlášení a odstranění uživatele ze session
    """
    session.pop('user', None)
    session.pop('role', None)
    flash("Úspěšně jste se odhlásili", "info")
    return redirect(url_for("index"))


# blueprint pro uživatelský profil
user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/")
def profile():
    """
    pokud uzivatel neni prihlasen vypise se flash message
    pokud je uzivatel prihlasen bude redirectnut na user.html
    """
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))
    return render_template("user.html", username=session['user'])