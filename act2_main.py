from flask import Flask,render_template,request
from act2_compra import Compra

app = Flask(__name__)

@app.route("/cinepolis")
def cinepolis():
    
    
    return render_template("cinepolis.html")

def compra():
    boletos = request.form.get('cantidadB')
    nombre = request.form.get('nombre')
    compradores = request.form.get('cantidadC')
    tarjeta = request.form.get('tarjeta')
    
def calcularPrecio(tarjeta,boletos,compradores):
    objC = Compra();
    p = 0
    t = 0
    
    
        
    if (boletos < 5):
        p = objC.compraB(boletos)
    
    if (boletos <= 7 & boletos > 3):
        p = p * 1.10
        
       
        

    

if __name__ == '__main__':
    app.run(debug=True, port=5000)