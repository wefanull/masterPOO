import json
import figuras_random 
import dibuja
import dibujarClima
from flask import Flask, json, render_template, Response, request
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html')

@app.route('/clima', methods=['GET'])
def clima():
    return render_template('clima.html')

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

@app.route('/dibujarClima', methods=('GET',))
def dc():
    ciudad = request.args.get('ciudad', default='Toluca')
    r = Response(response=dibujarClima.genera_imagen(ciudad), status=200, mimetype="image/png")
    r.headers["Content-Type"] = "image/png"
    return r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
