from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv


app = Flask(__name__)
mysql = MySQL(app)

class Conexion:    
    def __init__(self, MYSQL_HOST=None, MYSQL_PORT=None, MYSQL_USER=None, MYSQL_PASSWORD=None, MYSQL_DB=None):
        self.MYSQL_HOST = MYSQL_HOST or os.getenv("MYSQL_HOST") 
        self.MYSQL_PORT = int(os.getenv("MYSQL_PORT"))  
        self.MYSQL_USER = MYSQL_USER or os.getenv("MYSQL_USER")  
        self.MYSQL_PASSWORD = MYSQL_PASSWORD or os.getenv("MYSQL_PASSWORD")  
        self.MYSQL_DB = MYSQL_DB or os.getenv("MYSQL_DB")  