from flask import Flask, render_template
from iniciosesion.login import Login
from registrarusuario.registrar import Registrar
from olvidocontrasenia.olvido import Olvidocontrasenia
from gestionIndexInterno.indexInterno import IndexInterno
from gestionMapa.mapa import Mapa
import folium
import os
import logging


app = Flask(__name__)


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
        mapa = folium.Map(location=[4.611, -74.08175], zoom_start=6)
        if  not os.path.exists('static'):
            os.makedirs('static')
        mapa.save('static/mapa_con_marcadores.html')
        logging.info("Mapa guardado correctamente en 'static/mapa_con_marcadores.html'")
    except Exception as e:
            logging.error(f"Error al guardar el mapa: {e}")


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
