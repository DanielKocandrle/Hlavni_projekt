from flask import render_template, request, redirect, flash, url_for

from app.auth import bp as auth_bp

from app.register import bp as register_bp

from app import app

from os import path

from app.db import create_db

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__":
    if not path.exists(app.config["DATABASE"]):
        print("inicializace databaze")
        with app.app_context():
            create_db()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(register_bp, url_prefix="/register")
    app.run(debug=True)
