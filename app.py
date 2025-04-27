from flask import Flask, render_template
from iniciosesion.login import Login
from registrarusuario.registrar import Registrar
from olvidocontrasenia.olvido import Olvidocontrasenia
from gestionIndexInterno.indexInterno import IndexInterno
from gestionMapa.mapa import Mapa
import folium
import os
import logging
from flask_mysqldb import MySQL
import geocoder
import gpsd


from clases.conexionDB import Conexion
from clases.coordenada import Coordenada

app = Flask(__name__)

conex = Conexion()

# Cargar las variables de entorno desde el archivo .env
app.config['MYSQL_HOST'] = conex.MYSQL_HOST
app.config['MYSQL_PORT'] = conex.MYSQL_PORT 
app.config['MYSQL_USER'] = conex.MYSQL_USER
app.config['MYSQL_PASSWORD'] = conex.MYSQL_PASSWORD
app.config['MYSQL_DB'] = conex.MYSQL_DB

mysql = MySQL(app)

app.register_blueprint(Login) 
app.register_blueprint(Registrar)
app.register_blueprint(Olvidocontrasenia)
app.register_blueprint(IndexInterno) 
app.register_blueprint(Mapa) 


valid = False
app.secret_key = 'mysecretkey'

@app.route('/')
def default():
    url_get_mapa()
    generar_mapa()
    return render_template('./index/index.html')

def url_get_mapa():
    try:
            # g = geocoder.ip('me')
            # lat, lng = g.latlng

            gpsd.connect()
            packet = gpsd.get_current()
            lat, lon = packet
            print((packet.lat, packet.lon)) 

            if lat is not None and lon is not None:
                InicializaCoordenada = Coordenada(lat, lon)
                InicializaCoordenada.RegistrarCoordenada()
    except Exception as e:
        logging.error(f"Error al visualizar las coordenadas: {e}")


def generar_mapa():
    try:
        if  not os.path.exists('static'):
            os.makedirs('static')
        else:
            # # Obtener ubicación aproximada por IP
            # g = geocoder.ip('me')
            # lat, lon = g.latlng

            # mapa1 = folium.Map(location=[lat, lon], zoom_start=6)
            # folium.Marker(
            #     location=[lat, lon],
            #     popup="¡Estás aquí!",
            #     icon=folium.Icon(color="red", icon="user")
            # ).add_to(mapa1)

            # folium.Circle(
            #     location=[lat, lon],
            #     radius=1000,  # 1km de radio (ajústalo)
            #     color="#3186cc",
            #     fill=True
            # ).add_to(mapa1)


            xy = Coordenada.ConsultarCoordenada()
            mapa = folium.Map(location=xy[0], zoom_start=6)
            for lat, lon in xy:
                folium.Marker([lat, lon], popup="Visita sitio").add_to(mapa)
            mapa.save('static/mapa_con_marcadores.html')
    except Exception as e:
        logging.error(f"Error al visualizar las coordenadas: {e}")


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
