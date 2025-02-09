from flask import Flask, render_template
from iniciosesion.login import Login
from registrarusuario.registrar import Registrar
from olvidocontrasenia.olvido import Olvidocontrasenia


app = Flask(__name__)


app.register_blueprint(Login) 
app.register_blueprint(Registrar)
app.register_blueprint(Olvidocontrasenia)

valid = False
app.secret_key = 'mysecretkey'

@app.route('/')
def default():
    return render_template('./index/index.html')


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
