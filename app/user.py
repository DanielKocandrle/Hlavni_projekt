from flask import Blueprint, render_template, session, flash, redirect, url_for

user_bp = Blueprint("user", __name__, url_prefix="/user")

# definice routy pro user stranku
@user_bp.route("/")
def profile():
    if 'user' not in session:
        flash("Nejste přihlášeni!", "warning") #pokud user neni prihlasen, vypise se flash message uzivatel neni prihlasen
        return redirect(url_for("auth.login"))
    return render_template("user.html", username=session['user'])
