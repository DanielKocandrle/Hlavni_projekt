import sqlite3
from flask import current_app  # importovani momentalni instance flasku

# funkce pro vytvoreni databaze a inicializaci schematu
def create_db():
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:  # pripojeni k databazi
        with open(current_app.config["DB_SCHEME"]) as scheme:  # otevre soubor se schematem databaze
            conn.executescript(scheme.read())  # spusti sql skript pro vytvoreni tabulek
            conn.commit()  # ulozi zmeny

# yykonání SQL příkazu s volitelnými parametry
def execute(command, params=None):
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:  # pripojení k databázi
        if params:
            result = conn.execute(command, params).fetchall()  # spusti sql prikaz s parametry a ziska vsechny vysledky
        else:
            result = conn.execute(command).fetchall()  # spusti sql prikaz bez parametru a ziska vsechny vysledky
        conn.commit()  # ulozi zmeny
    return result  # vrati vysledky
