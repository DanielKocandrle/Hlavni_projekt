import sqlite3
from flask import current_app  # importovani momentalni instance flasku

# funkce pro vytvoreni databaze a inicializaci schematu
def create_db():
    """
    pripojeni k databazi
    otevre soubor se schematem databaze
    spusti sql skript pro vytvoreni tabulek
    ulozi zmeny
    """
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:
        with open(current_app.config["DB_SCHEME"]) as scheme:
            conn.executescript(scheme.read())
            conn.commit()

# yykonání SQL příkazu s volitelnými parametry
def execute(command, params=None):
    """
    pripojení k databázi
    spusti sql prikaz s parametry a ziska vsechny vysledky
    spusti sql prikaz bez parametru a ziska vsechny vysledky
    ulozi zmeny
    vrati vysledky
    """
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:
        if params:
            result = conn.execute(command, params).fetchall()
        else:
            result = conn.execute(command).fetchall()
        conn.commit()
    return result
