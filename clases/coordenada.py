from flask import Flask
from flask_mysqldb import MySQL
from clases.auditoria import Auditoria
from clases.conexionDB import Conexion
import os
from dotenv import load_dotenv

app = Flask(__name__)
mysql = MySQL(app)


class Coordenada:
    def __init__(self, lat, lng):
        self.lat = lat  # Corregido: eliminé la coma aquí
        self.lng = lng  # Corregido: eliminé la coma aquí
      
    def RegistrarCoordenada(self):
        auditoria = Auditoria('yosman.reyes')  # Ejemplo de inicialización de Auditoria
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO registro_coordenadas (lat, lng, Maquina_graba, Fecha_graba) VALUES (%s, %s, %s, %s)", (self.lat, self.lng, auditoria.Maquina_graba, auditoria.Fecha_graba))
        mysql.connection.commit()
        cur.close()

   