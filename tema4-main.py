from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Main"

@app.route("/user/<string:user>")
def user(user):
    return "Hello, World : {}".format(user)

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero : {}".format(n)

@app.route("/users/<int:id>/<string:name>")
def users(id , name):
    return "ID : {} | NOMBRE : {}".format(id , name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1 , n2):
    return "La suma es : {}".format(n1 + n2)


if __name__ == '__main__':
    app.run(debug=True)