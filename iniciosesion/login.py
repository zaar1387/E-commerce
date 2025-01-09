from flask import Blueprint, Flask, render_template, request, session, json, redirect, url_for


Login = Blueprint("login", __name__)

@Login.route('/login', methods=['GET'])
def login():
    return render_template('./iniciosesion/login.html')