import sqlite3
from sqlite3 import IntegrityError

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import execute

bp = Blueprint("register", __name__, url_prefix="/register")

@bp.route("/register", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Must provide username and password')

        try:
            command = "INSERT INTO users (username, password) VALUES (?, ?)"
            result = execute(command, (username, password))
            flash("Úspěšně jste se registroval", "success")
            return redirect(url_for("auth.login"))
        except sqlite3.IntegrityError:
            flash("Uživatelské jméno už je zabrané, vyberte prosím jiné", "danger")
            return redirect(url_for("register.login"))


    return render_template("register.html")