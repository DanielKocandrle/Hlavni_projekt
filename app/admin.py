from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Hlavní admin stránka
@admin_bp.route("/")
def admin():
    """
    Pokud uživatel není přihlášen nebo nemá roli 'admin', přesměruje ho na přihlašovací stránku.
    """
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning")
        return redirect(url_for("auth.login"))

    if session['role'] != 'admin':
        flash("Nemáte dostatečná práva pro přístup na tuto stránku.", "danger")
        return redirect(url_for("index"))

    return render_template("users.html")

# Seznam uživatelů
@admin_bp.route("/users", methods=("GET", "POST"))
def list_users():
    """
    Získá všechny uživatele a předá je do šablony.
    """
    if 'user' not in session or session.get('role') != 'admin':
        flash("Přístup odepřen.", "danger")
        return redirect(url_for("index"))

    command = "SELECT username, role FROM users"
    result = db.execute(command)
    return render_template("users.html", users=result)

@admin_bp.route("/delete_user/<username>", methods=["POST"])
def delete_user(username):
    """
    Odstraní uživatele z databáze podle uživatelského jména, pokud to není přihlášený uživatel.
    """
    if 'user' not in session or session.get('role') != 'admin':
        flash("Přístup odepřen.", "danger")
        return redirect(url_for("index"))

    # Získání přihlášeného uživatele
    logged_in_user = session.get('user')

    # Kontrola, zda se uživatel pokouší smazat svůj vlastní účet
    if logged_in_user == username:
        flash("Nemůžete smazat svůj vlastní účet.", "danger")
        return redirect(url_for("admin.list_users"))

    # Odstranění uživatele
    command = "DELETE FROM users WHERE username = :username"
    db.execute(command, {"username": username})
    flash(f"Uživatel {username} byl úspěšně smazán.", "success")
    return redirect(url_for("admin.list_users"))

@admin_bp.route("/change_password/<username>", methods=["GET", "POST"])
def change_password(username):
    """
    Umožní adminovi změnit heslo pro konkrétního uživatele.
    """
    if 'user' not in session or session.get('role') != 'admin':
        flash("Přístup odepřen.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        new_password = request.form["new_password"]

        # Příkaz pro aktualizaci hesla uživatele
        command = "UPDATE users SET password = :password WHERE username = :username"
        db.execute(command, {"password": new_password, "username": username})
        flash(f"Heslo uživatele {username} bylo úspěšně změněno.", "success")
        return redirect(url_for("admin.list_users"))

    return render_template("change_password.html", username=username)
