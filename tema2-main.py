from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '!!!Hola Lola¡¡¡'

@app.route("/hola")
def hola():
    return "HOOOOLAAA"

@app.route("/mundo")
def mundo():
    return "Mundo"


if __name__ == '__main__':
    app.run(debug=True)