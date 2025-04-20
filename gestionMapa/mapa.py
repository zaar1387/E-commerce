import folium
import os
import logging
from flask import Blueprint, request, json
from clases.conexionDB import Conexion
from clases.coordenada import Coordenada
from flask_mysqldb import MySQL


Mapa = Blueprint("mapa", __name__)


@Mapa.route('/url_get_mapa', methods=["POST"])
def url_get_mapa():
    try:
        if request.method == 'POST':
            array = request.form.to_dict() 
            lat = array['coordinates[lat]']
            lng = array['coordinates[lng]']
            if lat is not None and lng is not None:
                InicializaCoordenada = Coordenada(lat, lng)
                InicializaCoordenada.RegistrarCoordenada()
                return json.dumps({'status': 1, 'data': 1})
            else:
                return json.dumps({'error': 'Coordenadas no proporcionadas correctamente'}), 400
    except Exception as e:
        print("Error en la función url_get_mapa:", e)
        return json.dumps({'error': str(e)}), 500


def generar_mapa():
    try:
        mapa = folium.Map(location=[4.599860, -74.162560], zoom_start=13)
        if  not os.path.exists('static'):
            os.makedirs('static')
            mapa.save('static/mapa_con_marcadores.html')
            logging.info("Mapa guardado correctamente en 'static/mapa_con_marcadores.html'")
    except Exception as e:
            logging.error(f"Error al guardar el mapa: {e}")
    
       