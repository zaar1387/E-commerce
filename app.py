from flask import Flask, render_template

app = Flask(__name__)

valid = False
app.secret_key = 'mysecretkey'

@app.route('/')
def default():
    return render_template('./index/index.html')


if __name__ == '__main__': 
    app.run(host="0.0.0.0", use_debugger=True, use_reloader=True)
