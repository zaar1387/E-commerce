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
from clases.conexionDB import Conexion

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
    generar_mapa()
    return render_template('./index/index.html')

def generar_mapa():
    try:
        # cur = mysql.connection.cursor()
        # query = "SELECT a.lat, a.lng, a.Fecha_graba FROM registro_coordenadas a"
        # cur.execute(query)
        # results = query.fetchall()
        # logging.debug(f"Datos obtenidos de la base de datos: {results}")
        # if results:
        #     for (latitud, longitud, fecha) in results:
        #         logging.debug(f"Añadiendo marcador: Latitud={latitud}, Longitud={longitud}, Fecha={fecha}")
        #         try:
        #             folium.Marker([latitud, longitud], popup=f'Fecha: {fecha}').add_to(mapa)
        #         except Exception as e:
        #             logging.error(f"Error al añadir marcador: {e}")
        # else:
        #     logging.info("No se obtuvieron resultados de la consulta.")

        mapa = folium.Map(location=[4.611, -74.08175], zoom_start=6)
        if  not os.path.exists('static'):
            os.makedirs('static')
        mapa.save('static/mapa_con_marcadores.html')
        logging.info("Mapa guardado correctamente en 'static/mapa_con_marcadores.html'")
    except Exception as e:
            logging.error(f"Error al guardar el mapa: {e}")


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
