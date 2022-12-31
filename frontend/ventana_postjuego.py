from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal



class Ventana_Postjuego(QWidget):

    senal_salir = pyqtSignal()
    senal_siguiente_nivel = pyqtSignal(int, object)

    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(43, 42, 52)")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(180, 40, 251, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 141, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.nivel = QtWidgets.QLabel(self)
        self.nivel.setGeometry(QtCore.QRect(400, 110, 47, 13))
        self.nivel.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.nivel.setText("")
        self.nivel.setObjectName("nivel")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 141, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(90, 210, 141, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(90, 260, 141, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(90, 310, 271, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.balas_restantes = QtWidgets.QLabel(self)
        self.balas_restantes.setGeometry(QtCore.QRect(400, 160, 47, 13))
        self.balas_restantes.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.balas_restantes.setText("")
        self.balas_restantes.setObjectName("balas_restantes")
        self.tiempo_restante = QtWidgets.QLabel(self)
        self.tiempo_restante.setGeometry(QtCore.QRect(400, 210, 47, 13))
        self.tiempo_restante.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.tiempo_restante.setText("")
        self.tiempo_restante.setObjectName("tiempo_restante")
        self.puntaje_total = QtWidgets.QLabel(self)
        self.puntaje_total.setGeometry(QtCore.QRect(400, 260, 47, 13))
        self.puntaje_total.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.puntaje_total.setText("")
        self.puntaje_total.setObjectName("puntaje_total")
        self.puntaje_obtenido = QtWidgets.QLabel(self)
        self.puntaje_obtenido.setGeometry(QtCore.QRect(400, 310, 47, 13))
        self.puntaje_obtenido.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Yu Gothic UI Semibold\";\n"
"")
        self.puntaje_obtenido.setText("")
        self.puntaje_obtenido.setObjectName("puntaje_obtenido")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(480, 30, 91, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../T2/Sprites/Aliens/Alien3.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.siguiente = QtWidgets.QPushButton(self)
        self.siguiente.setGeometry(QtCore.QRect(150, 400, 101, 23))
        self.siguiente.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(114, 104, 135);")
        self.siguiente.setObjectName("siguiente")

        self.salir = QtWidgets.QPushButton(self)
        self.salir.setGeometry(QtCore.QRect(370, 400, 101, 23))
        self.salir.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(114, 104, 135);")
        self.salir.setObjectName("salir")

        self.label_perder = QtWidgets.QLabel(self)
        self.label_perder.setGeometry(QtCore.QRect(200, 350, 221, 31))
        self.label_perder.setStyleSheet("background-color: rgb(212, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Yu Gothic UI Semibold\";")
        self.label_perder.setObjectName("label_perder")


        self.label.setText("RESUMEN DEL NIVEL")
        self.label_2.setText("Nivel actual")
        self.label_3.setText("Balas restantes")
        self.label_4.setText("Tiempo restante")
        self.label_5.setText("Puntaje total")
        self.label_6.setText("Puntaje obtenido en nivel")
        self.siguiente.setText("Siguiente nivel")
        self.salir.setText("Salir")

        self.salir.clicked.connect(self.cerrar)

    def mostrar(self, resultado, juego, espacio):
        self.juego = juego

        self.espacio = espacio
            
        if resultado:
            self.label_ganar = QtWidgets.QLabel(self)
            self.label_ganar.setGeometry(QtCore.QRect(200, 350, 221, 31))
            self.label_ganar.setStyleSheet("background-color: rgb(0, 154, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 10pt \"Yu Gothic UI Semibold\";")
            self.label_ganar.setObjectName("label_ganar")
            self.label_ganar.setText("¡Puedes dominar el siguiente nivel!")
            self.siguiente.clicked.connect(self.siguiente_nivel)
            

        elif not resultado:
            self.label_perder = QtWidgets.QLabel(self)
            self.label_perder.setGeometry(QtCore.QRect(200, 350, 221, 31))
            self.label_perder.setStyleSheet("background-color: rgb(212, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font: 10pt \"Yu Gothic UI Semibold\";")
            self.label_perder.setObjectName("label_perder")
            self.label_perder.setText("¡Perdiste! No puedes seguir jugando :(")

        self.nivel.setText(str(self.juego.nivel_actual))
        self.balas_restantes.setText(str(self.juego.balas))
        self.tiempo_restante.setText(str(self.juego.tiempo_res))
        self.puntaje_total.setText(str(self.juego.puntaje_t))
        self.puntaje_obtenido.setText(str(self.juego.puntaje_o))
        self.show()

    def cerrar(self):
        self.hide()
        self.senal_salir.emit()

    def siguiente_nivel(self):
        self.hide()
        self.juego.velocidad = [self.juego.velocidad[0] / (self.juego.ponderador),
        self.juego.velocidad[1] / (self.juego.ponderador)]
        self.juego.nivel_actual += 1
        self.juego.balas = self.juego.nivel_actual * 4
        self.juego.cantidad_aliens = self.juego.nivel_actual *2
        self.juego.tiempo = self.juego.tiempo * self.juego.ponderador 
        self.senal_siguiente_nivel.emit(self.espacio, self.juego)
        



