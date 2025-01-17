from flask import Blueprint, Flask, render_template, request, session, json, redirect, url_for


Registrar = Blueprint("registrar", __name__)

@Registrar.route('/registrar', methods=['GET'])
def registrar():
    return render_template('./registrarusuario/registrar.html')