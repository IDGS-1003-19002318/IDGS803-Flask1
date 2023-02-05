from flask import Flask,render_template,request,flash
from act2_compra import Compra

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/cinepolis")
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/resultadoCompra', methods=['POST'])
def resultadoCompra():
    res = compra()
    return render_template('resultadoCinepolis.html', res=res)
    
def compra():
    boletos = int(request.form.get('cantidadB'))
    nombre = request.form.get('nombre')
    compradores = int(request.form.get('cantidadC'))
    tarjeta = bool(request.form.get('tarjeta'))
    
    precio = calcularPrecio(tarjeta=tarjeta,boletos=boletos,compradores=compradores)
    
    return precio,nombre
    
def calcularPrecio(tarjeta,boletos,compradores):
    compra = Compra();
    p = 0
    residuo = boletos / 7
    if residuo == compradores or residuo < compradores:
        p = compra.compraB(boletos)
        if (boletos >= 5):
            p = p * 0.85    
        elif (boletos >= 3):
                p = p * 0.90
    else:
        flash('Una persona no puede comprar más de 7 boletas')

    if tarjeta:
        p = p * 0.90
    
    return p

if __name__ == '__main__':
    app.run(debug=True, port=5000)