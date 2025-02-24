from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'tajny_klic'  # Nutné pro funkčnost flash zpráv


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Jednoduché ověření uživatele
        if username == "admin" and password == "password":
            flash("Úspěšně jste se přihlásil!", "success")
            return redirect(url_for('home'))  # Přesměrování na hlavní stránku
        elif username == "admin":
            flash("Neúspěšné přihlášení", "warning")
        else:
            flash("Neúspěšné přihlášení", "error")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
