import sqlite3
from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import execute

# vytvoreni registracniho blueprintu
bp = Blueprint("register", __name__, url_prefix="/register")

# definice routy pro registraci
@bp.route("/register", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        username = request.form['username']  # ziskani uzivatelskeho jmena
        password = request.form['password']  # ziskani hesla z formulare

        if not username or not password:
            flash('Must provide username and password')

        try:
            # vlozeni noveho uzivatele do databaze
            command = "INSERT INTO users (username, password) VALUES (?, ?)"
            result = execute(command, (username, password))

            flash("Úspěšně jste se registroval", "success")
            return redirect(url_for("auth.login"))  # presmerovani

        except sqlite3.IntegrityError:
            # chyba pro uzivatele kdyz si vybere uzivatelske jmeno ktere uz v databazi existuje
            flash("Uživatelské jméno už je zabrané, vyberte prosím jiné", "danger")
            return redirect(url_for("register.login"))

    # pokud metoda get, zobrazi registracni stranku
    return render_template("register.html")
