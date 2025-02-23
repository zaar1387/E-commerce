from flask import Blueprint, Flask, render_template

IndexInterno = Blueprint("indexInterno", __name__)

@IndexInterno.route('/index', methods=['GET'])
def index():
    return render_template('./gestionIndexInterno/indexInterno.html')