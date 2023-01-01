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

class Ventana_Juego(QMainWindow):

    senal_tecla = pyqtSignal(object, object)
    senal_tiempo = pyqtSignal()
    senal_postjuego = pyqtSignal(bool, object, int)
    senal_explosion = pyqtSignal(object)
    senal_juego_end = pyqtSignal(int, object)

    def __init__(self):
        super().__init__()
        self.contador = 0

    def mostrar(self,espacio,juego):
        self.video_widget = QVideoWidget(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("BASEJUEGO.mp4")))
        self.player.setPosition(75000)
        self.player.setVolume(0)
        self.player.play()

        self.setCentralWidget(self.video_widget)
    
        self.espacio = espacio
        self.juego = juego
        self.mira_clase = Mira()
        self.mira_izq_clase = Mira()

        self.mira = QtWidgets.QLabel(self)
        self.mira.setGeometry(QtCore.QRect(220, 150 , 130, 90 ))
        self.mira.setPixmap(QtGui.QPixmap("../programa/data/mano_derecha.png"))
        self.mira.setScaledContents(True)
        self.mira.setObjectName("mano")
        self.mira.setStyleSheet("background-color: transparent;")
        self.mira.setAutoFillBackground(False)

        self.mira_izq = QtWidgets.QLabel(self)
        self.mira_izq.setGeometry(QtCore.QRect(180, 150 , 130, 90 ))
        self.mira_izq.setPixmap(QtGui.QPixmap("../programa/data/mano_izquierda.png"))
        self.mira_izq.setScaledContents(True)
        self.mira_izq.setObjectName("mano-izq")
        self.mira_izq.setStyleSheet("background-color: transparent;")
        self.mira_izq.setAutoFillBackground(False)

        self.cora1 = QtWidgets.QLabel(self)
        self.cora1.setGeometry(QtCore.QRect(30, 40, 80, 60 ))
        self.cora1.setScaledContents(True)
        self.cora1.setPixmap(QtGui.QPixmap("../programa/data/cora.png"))
        self.cora1.setStyleSheet("background-color: transparent;")
        self.cora1.setAutoFillBackground(False)

        self.cora2 = QtWidgets.QLabel(self)
        self.cora2.setGeometry(QtCore.QRect(140, 40, 80, 60 ))
        self.cora2.setScaledContents(True)
        self.cora2.setPixmap(QtGui.QPixmap("../programa/data/cora.png"))
        self.cora2.setStyleSheet("background-color: transparent;")
        self.cora2.setAutoFillBackground(False)

        self.cora3 = QtWidgets.QLabel(self)
        self.cora3.setGeometry(QtCore.QRect(250, 40, 80, 60 ))
        self.cora3.setScaledContents(True)
        self.cora3.setPixmap(QtGui.QPixmap("../programa/data/vida.png"))
        self.cora2.setStyleSheet("background-color: transparent;")
        self.cora2.setAutoFillBackground(False)

        self.lista = self.juego.crear_props()
        self.parapentes_cls = self.juego.crear_parapentes()
        
        self.parapentes_cls[0].y = 100
        self.parapentes_cls[1].y = 400
        self.parapentes_cls[2].y = 200
        self.parapentes_cls[3].y = 300

        self.alien5_clase = self.lista[0]
        self.alien6_clase = self.lista[1]
        self.alien7_clase = self.lista[2]
        self.alien5_clase.y = 500
        self.alien6_clase.y = 400
        self.alien7_clase.y = 200

        self.parapentes = []
        for i, p_cls in enumerate(self.parapentes_cls): # instanciar 4 parapentes
            parapente = QtWidgets.QLabel(self)
            parapente.setGeometry(QtCore.QRect(p_cls.x, p_cls.y, 300, 230 ))
            parapente.setText("")
            parapente.setScaledContents(True)
            parapente.setObjectName("parapente{}".format(i+1))
            if i > 0:
                parapente.setVisible(False)
            self.parapentes.append(parapente)

        self.explosion = QtWidgets.QLabel(self)
        self.explosion.setText("")
        self.explosion.setScaledContents(True)
        self.explosion.setVisible(False)

        self.explosion1 = QtWidgets.QLabel(self)
        self.explosion1.setText("")
        self.explosion1.setScaledContents(True)
        self.explosion1.setVisible(False)

        self.explosion2 = QtWidgets.QLabel(self)
        self.explosion2.setText("")
        self.explosion2.setScaledContents(True)
        self.explosion2.setVisible(False)

        self.mira.raise_()
        self.mira_izq.raise_()
        
        for i, p in enumerate(self.parapentes):
            p.setPixmap(QtGui.QPixmap("../programa/data/parapente{}.png".format(i+1)))

        self.nivel_superado = QtWidgets.QLabel(self)
        self.nivel_superado.setGeometry(QtCore.QRect(300, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nivel_superado.setFont(font)
        self.nivel_superado.setStyleSheet("color: rgb(255, 255, 255);")
        self.nivel_superado.setText("       ¡Nivel superado!")
        self.nivel_superado.hide()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.mover_prop)
        self.timer.start()

        self.timer3 = QTimer()
        self.timer3.singleShot(2000,self.crearParapente)

        self.timer4 = QTimer()
        self.timer4.singleShot(4000,self.crearParapente)

        self.timer5 = QTimer()
        self.timer5.singleShot(6000,self.crearParapente)

        self.alien5 = QtWidgets.QLabel(self)
        self.alien5.setGeometry(QtCore.QRect(1, self.lista[0].y, 300, 230 ))
        self.alien5.setScaledContents(True)
        self.alien5.setPixmap(QtGui.QPixmap("../programa/data/planta1_1.png"))

        self.alien6 = QtWidgets.QLabel(self)
        self.alien6.setGeometry(QtCore.QRect(1, self.lista[1].y, 300, 230 ))
        self.alien6.setScaledContents(True)
        self.alien6.setPixmap(QtGui.QPixmap("../programa/data/ave1_1.png"))

        self.alien7 = QtWidgets.QLabel(self)
        self.alien7.setGeometry(QtCore.QRect(1, self.lista[2].y, 300, 230 ))
        self.alien7.setScaledContents(True)
        self.alien7.setPixmap(QtGui.QPixmap("../programa/data/ave2_1.png"))
        
        self.showFullScreen()

    def crearParapente(self): # mostar parapente n
        for i, p in enumerate(self.parapentes):
            if not p.isVisible():
                self.parapentes_cls[i].x = 1
                p.setVisible(True)
                return

    
    def actualizar_movimiento(self, x , y, x2, y2):
        if self.juego.pausa:
            self.disparo()

            self.mira.move(x, y)
            self.mira_clase.izq_der = x
            self.mira_clase.subir_bajar = y

            self.mira_izq.move(x2, y2)
            self.mira_izq_clase.izq_der = x2
            self.mira_izq_clase.subir_bajar = y2

    def actualizar_prop(self, x, y, numero):
        if self.juego.pausa:
            if numero < 5:
                self.parapentes[numero-1].move(x, y)
            if numero == 5:
                self.alien5.move(x, y)

    def mover_prop (self):
        if self.juego.pausa:
            self.juego.senal_mover_prop.connect(self.actualizar_prop)
            for i in range(4):
                self.juego.mover(self.parapentes_cls[i])
            
            self.juego.mover(self.alien5_clase)
            self.juego.mover(self.alien6_clase)
            self.juego.mover(self.alien7_clase)
            self.senal_tecla.emit(self.mira_clase, self.mira_izq_clase)
            
    def tiempo_avanzar(self):
        self.senal_tiempo.emit()
    
    def tiempo_final(self, valor):
        self.tiempo.setValue(valor)
    
    def disparo(self):
        self.recta = QtCore.QRect(
            self.mira_clase.izq_der + 40, 
            self.mira_clase.subir_bajar + 25, 
            130, 
            90)

        self.recta_izq = QtCore.QRect(
            self.mira_izq_clase.izq_der + 40, 
            self.mira_izq_clase.subir_bajar + 25, 
            130, 
            90)

        for i, p_cls in enumerate(self.parapentes_cls):
            recta_parapente = QtCore.QRect( 
                p_cls.x, 
                p_cls.y, 
                300, 
                230)
            if self.recta.intersected(recta_parapente) or self.recta_izq.intersected(recta_parapente):
                self.senal_explosion.emit(p_cls)
                p_cls.alive = False
                self.parapentes[i].setVisible(False)
                self.parapentes[i].destroy()
            
        self.evaluar()

    def evaluar(self):

        if not self.parapentes_cls[0].alive and not self.parapentes_cls[1].alive and not self.parapentes_cls[2].alive and not self.parapentes_cls[3].alive: 
            self.juego.puntaje_o = 4 # TODO: Guardar puntaje adecuado
            self.cerrar()
        
    def cerrar(self):
        self.puntaje_obtenido = 0
        self.tiempo_res = 0
        self.juego = Juego()
        self.video_widget.destroy()
        self.player.stop()
        for p in self.parapentes:
            p.destroy()
        self.alien5.destroy()
        self.alien6.destroy()
        self.alien7.destroy()
        self.mira.destroy()
        self.mira_izq.destroy()
        self.senal_postjuego.emit(True, self.juego, 1)
        self.close()
        
    def explosion(self, x, y, contador):
        if contador == 1:
            self.explosion.setPixmap(QtGui.QPixmap("../programa/data/ex_1.png"))
            self.explosion.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.explosion.setVisible(True)

        elif contador == 2:
            self.explosion.hide()
            self.explosion1.setPixmap(QtGui.QPixmap("../programa/data/ex_2.png"))
            self.explosion1.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.explosion1.setVisible(True)

        elif contador == 3:
            self.explosion1.hide()
            self.explosion2.setPixmap(QtGui.QPixmap("../programa/data/ex_3.png"))
            self.explosion2.setGeometry(QtCore.QRect(x, y, 50, 60 ))
            self.explosion2.setVisible(True)
        
        elif contador == 4:
            self.explosion2.hide()

    def tiempo_actualizar(self):
        self.tiempo.setValue(self.juego.tiempo_res)




        












