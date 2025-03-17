from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import execute

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        command = "SELECT username FROM users WHERE username = ? AND password = ?"

        result = execute(command, (username, password))

        print(result)

        if result:
            flash("login successful", "success")
            return redirect(url_for("index"))
        else:
            flash("login failed", "danger")

    return render_template("login.html")