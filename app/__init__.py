from flask import Flask, render_template
from os import path
from app.db import create_db

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config["SECRET_KEY"] = "tajny_klic"
app.config["DATABASE"] = "database.sqlite"
app.config["DB_SCHEME"] = "scheme.sql"

@app.route("/")
def index():
    return render_template("index.html")