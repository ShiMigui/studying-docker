from flask import Flask # type: ignore
from flask_mysqldb import MySQL # type: ignore
from os import getenv

debug = True
port = 5000

DB_BASE = getenv("DB_BASE")
DB_HOST = getenv("DB_HOST")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")

app = Flask(__name__)
app.config["DEBUG"] = debug
# MYSQL CONFIG
app.config["MYSQL_DB"] = DB_BASE
app.config["MYSQL_HOST"] = DB_HOST
app.config["MYSQL_USER"] = DB_USER
app.config["MYSQL_PASSWORD"] = DB_PASS

print(f"{DB_BASE} {DB_HOST} {DB_PASS} {DB_USER}")

mysql = MySQL(app)