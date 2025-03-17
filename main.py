from flask import render_template, request, redirect, flash, url_for

from app import app, login

app.register_blueprint(login.bp)

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)
