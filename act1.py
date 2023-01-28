from flask import Flask
from flask import request 

app = Flask(__name__)


@app.route("/operasBas" , methods=['GET' , 'POST'])
def operasBas():
    if request.method == 'POST':
        optionone = int(request.form.get('operation'))
        
        num1=int(request.form.get('num1'))
        num2=int(request.form.get('num2'))

        if (optionone == 1):
            result = "La suma es : {}".format(num1 + num2)
        elif (optionone == 2):
            result = "La resta es : {}".format(num1 - num2)
        elif (optionone == 3):
            result = "La multiplicacion es : {}".format(num1 * num2)
        elif (optionone == 4):
            result = "La divicion es : {}".format(num1 / num2)

        return result
    else :
        return ''' <form action="/operasBas" method="POST">

            <label for="">SUMA:</label>
            <input type="radio" name="operation" value="1" >  <br>
            <label for="">RESTA:</label>
            <input type="radio" name="operation" value="2" ><br>
            <label for="">MULTIPLICACION:</label>
            <input type="radio" name="operation" value="3" ><br>
            <label for="">DIVICION:</label>
            <input type="radio" name="operation" value="4" ><br><br>

            <label for="">N1 :</label>  
            <input type="text" name="num1"> <br><br>
            <label for="">N2 :</label>
            <input type="text" name="num2"> <br><br>
            <label for="">Enviar</label>
            <input type="submit"  value="Enviar"> <br><br>
        </form> '''

if __name__ == '__main__':
    app.run(debug=True)