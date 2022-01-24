import os
from flask import jsonify, request, Flask, render_template
from flaskext.mysql import MySQL
import random

app = Flask(__name__)

mysql = MySQL()

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)

@app.route("/")
def main():
    liczba = str(random.randint(1,5))
    tekst = "teskt"
    autor = "autor"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT zart_id, tekst, autor FROM zarty.zarty_lista WHERE zart_id LIKE '''+liczba+'''; ''')
    for zart_id, tekst, autor in cursor.fetchall():
        zart_id = str(zart_id)
        tekst = str(tekst)
        autor = str(autor)
    return "<h1> STRONA Z ŻARTAMI </h1> <br>" + tekst + "<h3> Autor: " + autor + "</h3>" + "<a href=/>KOLEJNY ŻART</a>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
