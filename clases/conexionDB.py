from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv


app = Flask(__name__)
mysql = MySQL(app)

class Conexion:
    def __init__(self, MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB):
        self.MYSQL_HOST = os.getenv("MYSQL_HOST"),  #os.getenv("ORACLE_USER")
        self.MYSQL_PORT = int(os.getenv("MYSQL_PORT")),
        self.MYSQL_USER = os.getenv("MYSQL_USER"),
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD"),
        self.MYSQL_DB = os.getenv("MYSQL_DB"),
        
        # connection=mysql.connect(
        #     self.MYSQL_HOST = os.getenv("MYSQL_HOST"),  #os.getenv("ORACLE_USER")
        #     self.MYSQL_PORT = int(os.getenv("MYSQL_PORT")),
        #     self.MYSQL_USER = os.getenv("MYSQL_USER"),
        #     self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD"),
        #     self.MYSQL_DB = os.getenv("MYSQL_DB"),
        # )