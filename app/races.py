from flask import Blueprint, render_template, request, flash, redirect, url_for, session

from app.db import execute

races_bp = Blueprint("races", __name__, url_prefix="/races")

@races_bp.route("/", methods=("GET", "POST"))
def races():
    if 'user' not in session:
        flash("Musíte být přihlášeni.", "warning")
        return redirect(url_for("auth.login"))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        username = session['user']
        # Pokud execute vrací seznam všech výsledků, použij:
        user_result = execute("SELECT id FROM users WHERE username = ?", (username,))

        if not user_result:
            flash("Uživatel nebyl nalezen.", "danger")
            return redirect(url_for("races.races"))

        user_id = user_result[0][0]  # Přístup k první hodnotě v první n-tici

        command = "INSERT INTO races (name, description, user_id) VALUES (?, ?, ?)"
        execute(command, (name, description, user_id))
        flash("Závod byl úspěšně vytvořen.", "success")
        return redirect(url_for("races.races"))

    # Získání všech závodů
    command = "SELECT id, name, description, user_id FROM races"
    # ✅ Správně
    races_list = execute(command)
    return render_template("races.html", races=races_list, current_user=session['user'], role=session.get('role'))


@races_bp.route("/delete_race/<int:race_id>", methods=["POST"])
def delete_race(race_id):
    if 'user' not in session:
        flash("Musíte být přihlášeni.", "warning")
        return redirect(url_for("auth.login"))

    user = session['user']
    role = session.get('role')

    # Získání závodu
    command = "SELECT user_id FROM races WHERE id = ?"
    result = execute("SELECT user_id FROM races WHERE id = ?", (race_id,))

    if not result or not result[0]:
        flash("Závod neexistuje.", "danger")
        return redirect(url_for("races.races"))

    race_creator = result[0][0]  # Získá user_id

    if role == 'admin' or race_creator == session['user']:
        execute("DELETE FROM races WHERE id = ?", (race_id,))
        flash("Závod byl úspěšně smazán.", "success")
    else:
        flash("Nemáte oprávnění ke smazání tohoto závodu.", "danger")

    return redirect(url_for("races.races"))
