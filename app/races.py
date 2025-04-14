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

@races_bp.route("/delete_race/<int:index>", methods=["POST"])
def delete_race(index):
    """
    Smaže závod na základě indexu z session.
    """
    if 'races' in session:
        try:
            # Smažeme závod podle indexu
            session['races'].pop(index)
            session.modified = True  # nutné pro změny v session
            flash("Závod byl úspěšně smazán.", "success")
        except IndexError:
            flash("Závod nebyl nalezen.", "danger")
    else:
        flash("Není žádný závod k odstranění.", "danger")

    return redirect(url_for("races.races"))
