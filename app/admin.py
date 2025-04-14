from flask import Blueprint, render_template, session, flash, redirect, url_for

from app import db

from app import user

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# definice routy pro user stranku
@admin_bp.route("/")
def admin():
    """
    Pokud uživatel není přihlášen nebo nemá roli 'admin', přesměruje ho na přihlašovací stránku.
    """
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))

    # Kontrola, zda uživatel má roli 'admin'
    if session['role'] != 'admin':
        flash("Nemáte dostatečná práva pro přístup na tuto stránku.", "danger")
        return redirect(url_for("index"))

    return render_template("users.html")

@admin_bp.route("/users", methods=("GET", "POST"))
def list_users():
    # Získání seznamu uživatelů z databáze
    users = user.get.all()

    return render_template("users.html", users=users)
