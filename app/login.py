from readline import insert_text

from flask import Blueprint, flash, redirect, render_template, request, url_for

bp = Blueprint('login', __name__, url_prefix='/login')

USERS = {"pokuston": "kouzelnik", "admin": "password", "student": "zak"}

@bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            flash("Úspěšně jste se přihlásil!", "success")
            return redirect(url_for('index'))
        elif username == "admin":
            flash("Neúspěšné přihlášení", "warning")
        else:
            flash("Neúspěšné přihlášení", "error")

    return render_template("login.html")

