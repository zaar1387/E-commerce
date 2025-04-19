import folium
import os
import logging
from flask import Blueprint


Mapa = Blueprint("mapa", __name__)


def generar_mapa():
    try:
        mapa = folium.Map(location=[4.599860, -74.162560], zoom_start=13)
        # if  not os.path.exists('static'):
        #     os.makedirs('static')
        #     mapa.save('static/mapa_con_marcadores.html')
        #     logging.info("Mapa guardado correctamente en 'static/mapa_con_marcadores.html'")
        
        if  not os.path.exists('templates'):
            os.makedirs('templates')
            mapa.save('templates/gestionMapa/mapa_con_marcadores.html')
            logging.info("Mapa guardado correctamente en 'templates/gestionMapa/mapa_con_marcadores.html'")
    except Exception as e:
            logging.error(f"Error al guardar el mapa: {e}")
    
       