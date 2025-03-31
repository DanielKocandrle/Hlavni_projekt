from flask import Flask, render_template
from os import path
from app.db import create_db

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config["SECRET_KEY"] = "tajny_klic"
app.config["DATABASE"] = "database.sqlite" # konfigurace databazove
app.config["DB_SCHEME"] = "scheme.sql" #konfigururace schematu pro databazi


@app.route("/")
def index():
    """
    definice routy pro hlavni stranku
    """
    return render_template("index.html")