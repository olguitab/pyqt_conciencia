from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow)
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import pyqtSignal, QTimer
from backend.logica_juego import Mira
from parametros import PONDERADOR_ENTRENAMIENTO, PONDERADOR_INVASION, PONDERADOR_TUTORIAL
from parametros import  TIEMPO_TERMINATOR_DOG, DURACION_NIVEL_INICIAL
from PyQt5.QtMultimedia import  QSound
from PyQt5.QtWidgets import *
from PyQt5 import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import*
from backend.logica_juego import Juego

class Ventana_Juego2(QMainWindow):

    senal_tecla = pyqtSignal(object)
    senal_alien = pyqtSignal()
    senal_tiempo = pyqtSignal()
    senal_postjuego = pyqtSignal(bool, object, int)
    senal_explosion = pyqtSignal(object)



    def __init__(self):
        super().__init__()
        self.a1 = True
        self.a2 = True
        self.contador = 0


    def mostrar(self,espacio,juego):
        self.video_widget = QVideoWidget(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("BASEJUEGO.mp4")))
        self.player.setPosition(76000)
        self.player.play()


        self.setCentralWidget(self.video_widget)


        self.espacio = espacio
        self.juego = juego
        self.mira_clase = Mira()

        self.mira = QtWidgets.QLabel(self)
        self.mira.setGeometry(QtCore.QRect(200, 150 , 130, 90 ))
        self.mira.setPixmap(QtGui.QPixmap("../programa/data/mano_derecha.png"))
        self.mira.setScaledContents(True)
        self.mira.setObjectName("mano")

        self.mira_izq = QtWidgets.QLabel(self)
        self.mira_izq.setGeometry(QtCore.QRect(200, 150 , 130, 90 ))
        self.mira_izq.setPixmap(QtGui.QPixmap("../programa/data/mano_derecha.png"))
        self.mira_izq.setScaledContents(True)
        self.mira_izq.setObjectName("mano")

        self.cora1 =QLabel(self.video_widget)
        self.cora1.setGeometry(QtCore.QRect(30, 40, 80, 60 ))
        self.cora1.setScaledContents(True)
        self.cora1.setPixmap(QtGui.QPixmap("../programa/data/cora.png"))

        self.cora2 = QtWidgets.QLabel(self)
        self.cora2.setGeometry(QtCore.QRect(140, 40, 80, 60 ))
        self.cora2.setScaledContents(True)
        self.cora2.setPixmap(QtGui.QPixmap("../programa/data/cora.png"))
        self.cora2.setStyleSheet("background-color: transparent")
        self.cora2.setAutoFillBackground(False)

        self.cora3 = QtWidgets.QLabel(self)
        self.cora3.setGeometry(QtCore.QRect(250, 40, 80, 60 ))
        self.cora3.setScaledContents(True)
        self.cora3.setPixmap(QtGui.QPixmap("../programa/data/vida.png"))


        self.lista = self.juego.crear_aliens()
        self.alien1_clase = self.lista[0]
        self.alien2_clase = self.lista[1]
        self.alien3_clase = self.lista[2]
        self.alien4_clase = self.lista[3]
        self.alien1_clase.y = 100
        self.alien2_clase.y = 400
        self.alien3_clase.y = 200
        self.alien4_clase.y = 300


        self.alien1 = QtWidgets.QLabel(self)
        self.alien1.setGeometry(QtCore.QRect(self.lista[0].x, self.lista[0].y, 300, 230 ))
        self.alien1.setText("")
        self.alien1.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.alien1.setScaledContents(True)
        self.alien1.setObjectName("alien1")

        self.alien2 = QtWidgets.QLabel(self)
        self.alien2.setGeometry(QtCore.QRect(self.lista[1].x, self.lista[1].y, 300, 230 ))
        self.alien2.setText("")
        self.alien2.setScaledContents(True)
        self.alien2.setObjectName("alien2")
        self.alien2.setVisible(False)

        self.alien3 = QtWidgets.QLabel(self)
        self.alien3.setGeometry(QtCore.QRect(self.lista[0].x, self.lista[0].y, 300, 230 ))
        self.alien3.setText("")
        self.alien3.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.alien3.setScaledContents(True)
        self.alien3.setObjectName("alien3")
        self.alien3.setVisible(False)


        self.alien4 = QtWidgets.QLabel(self)
        self.alien4.setGeometry(QtCore.QRect(self.lista[1].x, self.lista[1].y, 300, 230 ))
        self.alien4.setText("")
        self.alien4.setScaledContents(True)
        self.alien4.setObjectName("alien4")
        self.alien4.setVisible(False)

        self.disparar = QtWidgets.QLabel(self)
        self.disparar.setText("")
        self.disparar.setScaledContents(True)
        self.disparar.setVisible(False)

        self.disparar1 = QtWidgets.QLabel(self)
        self.disparar1.setText("")
        self.disparar1.setScaledContents(True)
        self.disparar1.setVisible(False)

        self.disparar2 = QtWidgets.QLabel(self)
        self.disparar2.setText("")
        self.disparar2.setScaledContents(True)
        self.disparar2.setVisible(False)
        self.mira.raise_()
        self.mira_izq.raise_()
        
        self.alien1.setPixmap(QtGui.QPixmap("../programa/data/parapente1.png"))
        self.alien2.setPixmap(QtGui.QPixmap("../programa/data/parapente2.png"))
        self.alien3.setPixmap(QtGui.QPixmap("../programa/data/parapente3.png"))
        self.alien4.setPixmap(QtGui.QPixmap("../programa/data/parapente4.png"))

        self.nivel_superado = QtWidgets.QLabel(self)
        self.nivel_superado.setGeometry(QtCore.QRect(300, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nivel_superado.setFont(font)
        self.nivel_superado.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.nivel_superado.setText("       ¡Nivel superado!")
        self.nivel_superado.hide()

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.mover_prop)
        self.timer.start()

        self.timer2 = QTimer()
        self.timer2.setInterval(DURACION_NIVEL_INICIAL*1000)
        self.timer2.timeout.connect(self.cerrar)
        self.timer2.start()

        self.timer3 = QTimer()
        self.timer3.singleShot(2000,self.crear2)

        self.timer4 = QTimer()
        self.timer4.singleShot(4000,self.crear3)

        self.timer5 = QTimer()
        self.timer5.singleShot(6000,self.crear4)
        

        self.showFullScreen()


    def crear2(self):
        self.alien2_clase.x = 1
        self.alien2.setVisible(True)

    def crear3(self):
        self.alien3_clase.x = 1
        self.alien3.setVisible(True)

    def crear4(self):
        self.alien4_clase.x = 1
        self.alien4.setVisible(True)
    

    def actualizar_movimiento(self, x , y, x2, y2):
        if self.juego.pausa:
            self.disparo()
            self.mira.move(x, y)
            self.mira_izq.move(x2, y2)
            self.mira_clase.izq_der = x
            self.mira_clase.subir_bajar = y
 
    def actualizar_alien(self, x, y, numero):
        if self.juego.pausa:
            if numero == 1:
                self.alien1.move(x, y)
            elif numero == 2:
                self.alien2.move(x, y)
            elif numero == 3:
                self.alien3.move(x, y)
            elif numero == 4:
                self.alien4.move(x, y)

    def mover_prop (self):
        if self.juego.pausa:
            self.juego.senal_mover_prop.connect(self.actualizar_alien)
            self.juego.mover(self.alien1_clase)
            self.juego.mover(self.alien2_clase)
            self.juego.mover(self.alien3_clase)
            self.juego.mover(self.alien4_clase)
            self.senal_tecla.emit(self.mira_clase)
        

    def tiempo_avanzar(self):
        self.senal_tiempo.emit()
    
    def tiempo_final(self, valor):
        self.tiempo.setValue(valor)
    
    def disparo(self):
        self.recta = QtCore.QRect(
            self.mira_clase.izq_der + 40, self.mira_clase.subir_bajar + 25, 130, 90)
        self.alien1_comparar =QtCore.QRect( 
            self.alien1_clase.x, self.alien1_clase.y, 300, 230)
        self.alien2_comparar =QtCore.QRect(
            self.alien2_clase.x, self.alien2_clase.y, 300, 230)
        if self.recta.intersected(self.alien1_comparar):
            self.senal_explosion.emit(self.alien1_clase)
            self.alien1.hide()
            self.a1 = False

        if self.recta.intersected(self.alien2_comparar):
            self.senal_explosion.emit(self.alien2_clase)
            self.alien2.hide()
            self.a2 = False
        self.evaluar()
        

    def evaluar(self):
        if not self.a1 and not self.a2: 
            if len(self.lista) == 2:
                self.juego.puntaje_o = int(((self.juego.nivel_actual * 200 + 
                (self.juego.tiempo_res * 30 + self.juego.balas * 70) * self.juego.nivel_actual))
                /self.juego.ponderador)
            else:
                self.lista = self.lista[2:]
                self.a1 = True
                self.a2 = True
                self.alien1.show()
                self.alien2.show()

        
    def cerrar(self):
        self.puntaje_obtenido = 0
        self.tiempo_res = 0
        self.senal_postjuego.emit(False, self.juego, self.espacio)
        self.video_widget.destroy()
        self.player.stop()
        self.close()
        
    def explosion(self, x, y, contador):
        if contador == 1:
            self.disparar.setPixmap(QtGui.QPixmap("../programa/data/ex_1.png"))
            self.disparar.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.disparar.setVisible(True)

        elif contador == 2:
            self.disparar.hide()
            self.disparar1.setPixmap(QtGui.QPixmap("../programa/data/ex_2.png"))
            self.disparar1.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.disparar1.setVisible(True)

        elif contador == 3:
            self.disparar1.hide()
            self.disparar2.setPixmap(QtGui.QPixmap("../programa/data/ex_3.png"))
            self.disparar2.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.disparar2.setVisible(True)
        
        elif contador == 4:
            self.disparar2.hide()

    def tiempo_actualizar(self):
        self.tiempo.setValue(self.juego.tiempo_res)