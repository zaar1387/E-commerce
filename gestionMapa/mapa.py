from flask import Blueprint, request, json
from clases.conexionDB import Conexion
from clases.coordenada import Coordenada
from flask_mysqldb import MySQL
import geocoder
from flask import redirect

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
                return redirect('/')
            
    except Exception as e:
        print("Error en la función url_get_mapa:", e)
        return json.dumps({'error': str(e)}), 500