import sqlite3
from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import execute

# vytvoreni registracniho blueprintu
bp = Blueprint("register", __name__, url_prefix="/register")

# definice routy pro registraci
@bp.route("/register", methods=("GET", "POST"))
def login():
    """
     21 - ziskani uzivatelskeho jmena
     22 - ziskani hesla z formulare
     26 - vlozeni noveho uzivatele do databaze
     34 - chyba pro uzivatele kdyz si vybere uzivatelske jmeno ktere uz v databazi existuje
     38 - pokud metoda get, zobrazi registracni stranku
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Must provide username and password')

        try:
            command = "INSERT INTO users (username, password) VALUES (?, ?)"
            result = execute(command, (username, password))

            flash("Úspěšně jste se registroval", "success")
            return redirect(url_for("auth.login"))  # presmerovani

        except sqlite3.IntegrityError:
            flash("Uživatelské jméno už je zabrané, vyberte prosím jiné", "danger")
            return redirect(url_for("register.login"))

    return render_template("register.html")
