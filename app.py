from flask import Flask, render_template, json
from iniciosesion.login import Login
from registrarusuario.registrar import Registrar
from olvidocontrasenia.olvido import Olvidocontrasenia
from gestionIndexInterno.indexInterno import IndexInterno
from gestionMapa.mapa import Mapa
import folium
import os
import logging
from flask_mysqldb import MySQL
from telegram import Bot
from telegram.request import HTTPXRequest
import certifi
from dotenv import load_dotenv


import tracemalloc
tracemalloc.start()
import ssl


# Configurar la ruta de certificados SSL
os.environ['SSL_CERT_FILE'] = certifi.where()


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
# Token del bot 
token = "8001684220:AAFiTf0awnD3v4tsjCPGi4tTqf6_-wURrUs"
# ID del chat
chat_id = 893903335
# Crear un objeto Bot
bot = Bot(token=token)

valid = False
app.secret_key = 'mysecretkey'

@app.route('/')
def default():
    generar_mapa()
    return render_template('./index/index.html')


def generar_mapa():
    try:
        if  not os.path.exists('static'):
            os.makedirs('static')
        else:
            xy = Coordenada.ConsultarCoordenada()
            mapa = folium.Map(location=xy[0], zoom_start=6)
            for lat, lon in xy:
                folium.Marker([lat, lon], popup="Visita sitio").add_to(mapa)
            mapa.save('static/mapa_con_marcadores.html')
        
    except Exception as e:
        logging.error(f"Error al visualizar las coordenadas: {e}")


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
