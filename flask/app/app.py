import json
import figuras_random 
import dibuja
import clima
import dibujarClima
from flask import Flask, json, render_template, Response, request
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/figuras', methods=('GET', 'POST'))
def github():
    return json.dumps({
        "figuras": [
            {
                "nombre": "cuadrado",
                "lados": 4
            },
            {
                "nombre": "triangulo",
                "lados": 3
            },
            {
                "nombre": "circulo",
                "lados": 0
            }
        ]
    })
    
@app.route('/figuras_random', methods=('GET', 'POST'))
def fr():
    return figuras_random.figuras_random()

@app.route('/dibuja', methods=('GET', 'POST'))
def db():
    r = Response(response=dibuja.dibuja(), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

@app.route('/dibujarClima', methods=('GET', 'POST'))
def dc():
    r = Response(response=dibujarClima.dibuja_icono("01n"), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

@app.route('/clima', methods=('GET', 'POST'))
def clima():
    Ciudad = request.args.get('ciudad')
    return {
        "ciudad": Ciudad,
        "palo" : request.args.get('palo'),
        "piedra": request.args.get('piedra')
    }

#clima.Clima().extrae_relevantes('Toluca')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
