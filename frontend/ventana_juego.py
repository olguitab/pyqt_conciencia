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

    senal_tecla = pyqtSignal(object)
    senal_tecla_izq = pyqtSignal(object)
    senal_alien = pyqtSignal()
    senal_tiempo = pyqtSignal()
    senal_postjuego = pyqtSignal(bool, object, int)
    senal_explosion = pyqtSignal(object)
    senal_juego_end = pyqtSignal(int, object)



    def __init__(self):
        super().__init__()
        self.a1 = True
        self.a2 = True
        self.a3 = True
        self.a4 = True
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

        self.mira_izq = QtWidgets.QLabel(self)
        self.mira_izq.setGeometry(QtCore.QRect(180, 150 , 130, 90 ))
        self.mira_izq.setPixmap(QtGui.QPixmap("../programa/data/mano_izquierda.png"))
        self.mira_izq.setScaledContents(True)
        self.mira_izq.setObjectName("mano-izq")

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
        self.parapente1_cls = self.lista[0]
        self.parapente2_cls = self.lista[1]
        self.parapente3_cls = self.lista[2]
        self.parapente4_cls = self.lista[3]
        self.alien5_clase = self.lista[4]
        self.alien6_clase = self.lista[5]
        self.alien7_clase = self.lista[6]
        self.parapente1_cls.y = 100
        self.parapente2_cls.y = 400
        self.parapente3_cls.y = 200
        self.parapente4_cls.y = 300
        self.alien5_clase.y = 500
        self.alien6_clase.y = 400
        self.alien7_clase.y = 200


        self.parapente1 = QtWidgets.QLabel(self)
        self.parapente1.setGeometry(QtCore.QRect(self.lista[0].x, self.lista[0].y, 300, 230 ))
        self.parapente1.setText("")
        self.parapente1.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.parapente1.setScaledContents(True)
        self.parapente1.setObjectName("parapente1")

        self.parapente2 = QtWidgets.QLabel(self)
        self.parapente2.setGeometry(QtCore.QRect(self.lista[1].x, self.lista[1].y, 300, 230 ))
        self.parapente2.setText("")
        self.parapente2.setScaledContents(True)
        self.parapente2.setObjectName("parapente2")
        self.parapente2.setVisible(False)

        self.parapente3 = QtWidgets.QLabel(self)
        self.parapente3.setGeometry(QtCore.QRect(self.lista[0].x, self.lista[0].y, 300, 230 ))
        self.parapente3.setText("")
        self.parapente3.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.parapente3.setScaledContents(True)
        self.parapente3.setObjectName("parapente3")
        self.parapente3.setVisible(False)

        self.parapente4 = QtWidgets.QLabel(self)
        self.parapente4.setGeometry(QtCore.QRect(self.lista[1].x, self.lista[1].y, 300, 230 ))
        self.parapente4.setText("")
        self.parapente4.setScaledContents(True)
        self.parapente4.setObjectName("parapente4")
        self.parapente4.setVisible(False)

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
        
        self.parapente1.setPixmap(QtGui.QPixmap("../programa/data/parapente1.png"))
        self.parapente2.setPixmap(QtGui.QPixmap("../programa/data/parapente2.png"))
        self.parapente3.setPixmap(QtGui.QPixmap("../programa/data/parapente3.png"))
        self.parapente4.setPixmap(QtGui.QPixmap("../programa/data/parapente4.png"))

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

        #self.timer2 = QTimer()
        #self.timer2.setInterval(10000)
        #self.timer2.timeout.connect(self.cerrar)
        #self.timer2.start()

        self.timer3 = QTimer()
        self.timer3.singleShot(2000,self.crear2)

        self.timer4 = QTimer()
        self.timer4.singleShot(4000,self.crear3)

        self.timer5 = QTimer()
        self.timer5.singleShot(6000,self.crear4)

        self.alien5 = QtWidgets.QLabel(self)
        self.alien5.setGeometry(QtCore.QRect(1, self.lista[1].y, 300, 230 ))
        self.alien5.setScaledContents(True)
        self.alien5.setPixmap(QtGui.QPixmap("../programa/data/planta1_1.png"))

        self.alien6 = QtWidgets.QLabel(self)
        self.alien6.setGeometry(QtCore.QRect(1, self.lista[4].y, 300, 230 ))
        self.alien6.setScaledContents(True)
        self.alien6.setPixmap(QtGui.QPixmap("../programa/data/ave1_1.png"))

        self.alien7 = QtWidgets.QLabel(self)
        self.alien7.setGeometry(QtCore.QRect(1, self.lista[4].y, 300, 230 ))
        self.alien7.setScaledContents(True)
        self.alien7.setPixmap(QtGui.QPixmap("../programa/data/ave2_1.png"))
        

        self.showFullScreen()

    def crear2(self):
        self.parapente2_cls.x = 1
        self.parapente2.setVisible(True)

    def crear3(self):
        self.parapente3_cls.x = 1
        self.parapente3.setVisible(True)

    def crear4(self):
        self.parapente4_cls.x = 1
        self.parapente4.setVisible(True)
    
    def actualizar_movimiento(self, x , y):
        if self.juego.pausa:
            self.disparo()
            self.mira.move(x, y)
            self.mira_clase.izq_der = x
            self.mira_clase.subir_bajar = y

    def actualizar_movimiento_izq(self, x , y):
        if self.juego.pausa:
            self.disparo_izq()
            self.mira_izq.move(x, y)
            self.mira_izq_clase.izq_der = x
            self.mira_izq_clase.subir_bajar = y
 
    def actualizar_alien(self, x, y, numero):
        if self.juego.pausa:
            if numero == 1:
                self.parapente1.move(x, y)
            elif numero == 2:
                self.parapente2.move(x, y)
            elif numero == 3:
                self.parapente3.move(x, y)
            elif numero == 4:
                self.parapente4.move(x, y)
            elif numero == 5:
                self.alien5.move(x, y)

    def mover_prop (self):
        if self.juego.pausa:
            self.juego.senal_mover_prop.connect(self.actualizar_alien)
            self.juego.mover(self.parapente1_cls)
            self.juego.mover(self.parapente2_cls)
            self.juego.mover(self.parapente3_cls)
            self.juego.mover(self.parapente4_cls)
            self.juego.mover(self.alien5_clase)
            self.juego.mover(self.alien6_clase)
            self.juego.mover(self.alien7_clase)
            self.senal_tecla.emit(self.mira_clase)
            self.senal_tecla_izq.emit(self.mira_izq_clase)

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

        self.parapente1_comparar =QtCore.QRect( 
            self.parapente1_cls.x, self.parapente1_cls.y, 300, 230)
        self.parapente2_comparar =QtCore.QRect(
            self.parapente2_cls.x, self.parapente2_cls.y, 300, 230)
        self.parapente3_comparar =QtCore.QRect(
            self.parapente3_cls.x, self.parapente3_cls.y, 300, 230)
        self.parapente4_comparar =QtCore.QRect(
            self.parapente4_cls.x, self.parapente4_cls.y, 300, 230)

        if self.recta.intersected(self.parapente1_comparar):
            self.senal_explosion.emit(self.parapente1_cls)
            self.parapente1.setVisible(False)
            self.a1 = False
            self.parapente1.destroy()

        if self.recta.intersected(self.parapente2_comparar):
            self.senal_explosion.emit(self.parapente2_cls)
            self.parapente2.setVisible(False)
            self.a2 = False
            self.parapente2.destroy()

        if self.recta.intersected(self.parapente3_comparar):
            self.senal_explosion.emit(self.parapente3_cls)
            self.parapente3.setVisible(False)
            self.a3 = False
            self.parapente3.destroy()
        
        if self.recta.intersected(self.parapente4_comparar):
            self.senal_explosion.emit(self.parapente4_cls)
            self.parapente4.setVisible(False)
            self.a4 = False
            self.parapente4.destroy()
        self.evaluar()

    def disparo_izq(self):
        self.recta = QtCore.QRect(
            self.mira_izq_clase.izq_der + 40, self.mira_izq_clase.subir_bajar + 25, 130, 90)
        self.parapente1_comparar =QtCore.QRect( 
            self.parapente1_cls.x, self.parapente1_cls.y, 300, 230)
        self.parapente2_comparar =QtCore.QRect(
            self.parapente2_cls.x, self.parapente2_cls.y, 300, 230)
        self.parapente3_comparar =QtCore.QRect(
            self.parapente3_cls.x, self.parapente3_cls.y, 300, 230)
        self.parapente4_comparar =QtCore.QRect(
            self.parapente4_cls.x, self.parapente4_cls.y, 300, 230)

        if self.recta.intersected(self.parapente1_comparar):
            self.senal_explosion.emit(self.parapente1_cls)
            self.parapente1.setVisible(False)
            self.a1 = False

        if self.recta.intersected(self.parapente2_comparar):
            self.senal_explosion.emit(self.parapente2_cls)
            self.parapente2.setVisible(False)
            self.a2 = False

        if self.recta.intersected(self.parapente3_comparar):
            self.senal_explosion.emit(self.parapente3_cls)
            self.parapente3.setVisible(False)
            self.a3 = False
        
        if self.recta.intersected(self.parapente4_comparar):
            self.senal_explosion.emit(self.parapente4_cls)
            self.parapente4.setVisible(False)
            self.a4 = False
        self.evaluar()
        
    def evaluar(self):
        if not self.a1 and not self.a2 and not self.a3 and not self.a4: 
            self.juego.puntaje_o = 4 # TODO: Guardar puntaje adecuado
            self.cerrar()
            """
            if len(self.lista) == 2:
                self.juego.puntaje_o = int(
                    (
                        (self.juego.nivel_actual * 200 + 
                        (
                            self.juego.tiempo_res * 30 + self.juego.balas * 70
                        ) * self.juego.nivel_actual)
                    ) / self.juego.ponderador)
            else:
                self.lista = self.lista[2:]
                self.a1 = True
                self.a2 = True
                self.a3 = True
                self.a4 = True
                self.parapente1.show()
                self.parapente2.show()
                self.parapente3.show()
                self.parapente4.show()
            """
        
    def cerrar(self):
        self.puntaje_obtenido = 0
        self.tiempo_res = 0
        self.juego = Juego()
        self.video_widget.destroy()
        self.player.stop()
        self.parapente1.destroy()
        self.parapente2.destroy()
        self.parapente3.destroy()
        self.parapente4.destroy()
        self.alien5.destroy()
        self.alien6.destroy()
        self.alien7.destroy()
        self.mira.destroy()
        self.mira_izq.destroy()
        self.senal_postjuego.emit(True, self.juego, 1)
        #self.close()
        
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




        












