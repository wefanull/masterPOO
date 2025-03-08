from multimethod import multimethod
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QPoint
import math

# Clase Geometrica, metaclase

class Geometrica:

    def __init__(self,painter:QtGui.QPainter, x, y):
        self.x = x
        self.y = y
        self.painter = painter
        print(f"Se ha creado una figura geometrica en la posicion ({self.x},{self.y}) ")
        
    def moverse(self):
        self.x += 10
        self.y += 10
        print(f"Se ha movido la figura geometrica a la posicion ({self.x},{self.y}) ")
        
# Clase Circulo hereda de Geometrica

class Circulo(Geometrica):
    
    def __init__(self,painter:QtGui.QPainter, x, y, radio):
        super().__init__(painter,x,y)    
        self.radio = radio
        
    @multimethod    
    def dibujar(self):
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)

    @multimethod    
    def dibujar(self, color:Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)


# Clase Circulo hereda de Geometrica

class Cuadrado(Geometrica):
    
    def __init__(self,painter:QtGui.QPainter, x, y, lado):
        super().__init__(painter,x,y)    
        self.lado = lado
        
    @multimethod    
    def dibujar(self, color:Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawRect(self.x,self.y,self.lado,self.lado)

    @multimethod    
    def dibujar(self):
        self.painter.drawRect(self.x,self.y,self.lado,self.lado)

class TrianguloEquilatero(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, lado):
        super().__init__(painter, x, y)
        self.lado = lado
        self.puntos = self.calcular_puntos()

    def calcular_puntos(self):
        altura = (math.sqrt(3) / 2) * self.lado
        x1 = self.x - self.lado / 2
        y1 = self.y + altura / 3
        x2 = self.x + self.lado / 2
        y2 = self.y + altura / 3
        x3 = self.x
        y3 = self.y - (2 * altura) / 3
        return [(x1, y1), (x2, y2), (x3, y3)]

    def dibujar(self, color: Qt.GlobalColor = Qt.GlobalColor.black):
        self.painter.setBrush(color)
        self.painter.drawPolygon(QtGui.QPolygon([
            QPoint(int(p[0]), int(p[1])) for p in self.puntos
        ]))

class Pentagono(Geometrica):
    def __init__(self, painter: QtGui.QPainter, x, y, radio):
        super().__init__(painter, x, y)
        self.radio = radio
        self.puntos = self.calcular_puntos()
        print(f" con radio {self.radio}")

    def calcular_puntos(self):
        puntos = []
        for i in range(5):
            angulo = 2 * math.pi * i / 5
            px = self.x + self.radio * math.cos(angulo)
            py = self.y + self.radio * math.sin(angulo)
            puntos.append((px, py))
        return puntos

    def dibujar(self, color: Qt.GlobalColor = Qt.GlobalColor.black):
        self.painter.setBrush(color)
        self.painter.drawPolygon(QtGui.QPolygon([
            QPoint(int(p[0]), int(p[1])) for p in self.puntos
        ]))