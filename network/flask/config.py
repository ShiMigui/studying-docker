from flask import Flask # type: ignore
from flask_mysqldb import MySQL # type: ignore

debug = True
port = 5000

app = Flask(__name__)
app.config["DEBUG"] = debug
# MYSQL CONFIG
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_DB"] = 'flaskAPI'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_HOST"] = 'mysql_flask'

mysql = MySQL(app)