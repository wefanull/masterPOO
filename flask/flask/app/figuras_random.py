import json,random

def figuras_random():
    figuras=[]
    nombres = ["cuadrado", "triangulo", "circulo", "pentagono"]
    color = ["rojo", "verde", "azul", "amarillo", "naranja", "rosa", "negro", "blanco"]
    for i in range(0, random.randint(2, 10)):
        figuras.append({
            "nombre": nombres[random.randint(0, 2)],
            "color": color[random.randint(0, 7)],
            "x": random.randint(0, 400),
            "y": random.randint(0, 400),
            "medida": random.randint(0, 100)
        })
    return json.dumps(figuras)