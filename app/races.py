from flask import Blueprint, render_template, request, flash, redirect, url_for, session

races_bp = Blueprint("races", __name__, url_prefix="/races")

@races_bp.route("/", methods=("GET", "POST"))
def races():
    # inicializace seznamu závodů, pokud neexistuje
    if 'races' not in session:
        session['races'] = []

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        race = {'name': name, 'description': description}
        session['races'].append(race)
        session.modified = True  # nutné, aby Flask věděl, že jsme session změnili

        flash("Úspěšně jste vytvořil příspěvek", "success")
        return redirect(url_for("races.races"))

    races_list = session.get('races', [])
    return render_template("races.html", races=races_list)