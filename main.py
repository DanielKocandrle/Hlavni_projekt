from flask import render_template, request, redirect, flash, url_for

from app.auth import bp as auth_bp

from app.register import bp as register_bp

from app import app

from os import path

from app.db import create_db

from app.user import user_bp

 # hlavni blok pro spusteni aplikace
if __name__ == "__main__":
    # kontrola jestli existuje databazovy soubor a jestli ne tak se vytvori
    if not path.exists(app.config["DATABASE"]):
        print("inicializace databaze")
        with app.app_context():
            create_db()  # vytvoreni databazovych tabulek

    # registrace blueprintů pro prihlaseni a registraci
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(register_bp, url_prefix="/register")

    app.register_blueprint(user_bp, url_prefix="/user")

    app.run(debug=True)
