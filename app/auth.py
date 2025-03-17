from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import execute

# vytvoreni prihlasovaciho blueprintu
bp = Blueprint("auth", __name__, url_prefix="/auth")

# definice routy pro prihlaseni
@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form['username']  # ziskani uzivatelskeho jmena
        password = request.form['password']  # ziskani hesla z formulare

        # vybere noveho uzivatele z databaze
        command = "SELECT username FROM users WHERE username = ? AND password = ?"

        result = execute(command, (username, password))

        if result:
            flash("Přihlášení úspěšné", "success")
            return redirect(url_for("index"))
        else:
            flash("Špatné uživatelské jméno nebo heslo", "danger")

    return render_template("login.html")