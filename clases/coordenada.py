from flask import Flask
from flask_mysqldb import MySQL
from clases.auditoria import Auditoria
from clases.conexionDB import Conexion
import os
from dotenv import load_dotenv
import folium
import logging


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

    def ConsultarCoordenada(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT lat, lng FROM registro_coordenadas")
        results = cur.fetchall()
        cur.close()
        if results:
            for (latitud, longitud, fecha) in results:
                # logging.debug(f"Añadiendo marcador: Latitud={latitud}, Longitud={longitud}, Fecha={fecha}")
                try:
                    mapa = folium.Map(location=[latitud, longitud], zoom_start=6)
                    folium.Marker([latitud, longitud], popup=f'Fecha: {fecha}').add_to(mapa)
                except Exception as e:
                    logging.error(f"Error al añadir marcador: {e}")
        else:
            logging.info("No se obtuvieron resultados de la consulta.")
        return results

   