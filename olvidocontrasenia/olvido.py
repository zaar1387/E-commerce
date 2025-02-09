from flask import Blueprint, Flask, render_template


Olvidocontrasenia = Blueprint("olvidocontrasenia", __name__)

@Olvidocontrasenia.route('/olvido', methods=['GET'])
def olvido():
    return render_template('./olvidocontrasenia/olvidocontrasenia.html')