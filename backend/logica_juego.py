from random import random, randint
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject,  QTimer
from PyQt5 import QtCore, QtGui
from parametros import VELOCIDAD_PROPS, DURACION_NIVEL_INICIAL
from os import path
from random import randint
from PyQt5.QtMultimedia import QMediaPlayer, QSound
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication

class xy_pos():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Mira(QObject):
    def __init__(self):
        super().__init__()
        self.subir_bajar = 150
        self.izq_der = 300
        self.jugador = QMediaPlayer
        self.palabra = ""

class Mano(QLabel):
    def __init__(self, imageUrl):
        super().__init__()
        self.setGeometry(QtCore.QRect(220, 150 , 130, 90 ))
        self.setPixmap(QtGui.QPixmap(imageUrl))
        self.setScaledContents(True)
        self.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.subir_bajar = 150
        self.izq_der = 300

class Corazon(QLabel):
    def __init__(self, xy_pos):
        super().__init__()
        self.setGeometry(QtCore.QRect(xy_pos.x, xy_pos.y, 80, 60 ))
        self.setScaledContents(True)
        self.setPixmap(QtGui.QPixmap("../programa/data/vida.png"))
        self.setStyleSheet("background-color:  rgba(0,0,0,0%);")

class Parapente(QLabel):
    id = 1
    def __init__(self, xy_pos, id):
        super().__init__()
        self.id = id+1
        self.setGeometry(QtCore.QRect(xy_pos.x, xy_pos.y, 300, 230 ))
        self.setText("")
        self.setScaledContents(True)
        self.setObjectName("parapente{}".format(id))

class Planta(QLabel):
    # TODO: Completar clase planta
    id = 1
    def __init__(self, xy_pos, id):
        super().__init__()
        self.id = id+1
        self.setGeometry(QtCore.QRect(xy_pos.x, xy_pos.y, 300, 230 ))
        self.setText("")
        self.setScaledContents(True)
        self.setObjectName("planta1_{}".format(id))



class Prop(QObject):
    #60,50
    #640,380

    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = randint(0,330)
        self.velocidad = [VELOCIDAD_PROPS[0],VELOCIDAD_PROPS[1]]
        self.numero = 0
        self.espacio = [self.x, self.y , 60, 50]
        self.alive = True
        self.imageUrl = ""

class Jugador(QObject):

    def __init__(self, usuario, puntaje):
        self.usuario = usuario
        self.puntaje = puntaje


class Juego (QObject):

    senal_mover_prop = pyqtSignal(int, int, int)
    senal_boom = pyqtSignal(int, int, int)
    senal_actualizar = pyqtSignal()
    senal_mover_mira = pyqtSignal(int, int, int, int)
    senal_disparo = pyqtSignal()

    def __init__(self):

        super().__init__()

        self.nivel_actual = 1
        self.cantidad_aliens = 2 * self.nivel_actual
        self.balas = 2 * self.cantidad_aliens
        self.dificultad = 0
        self.contador_explosion = 1
        self.puntaje = 0
        self.contador = 0
        self.tiempo = DURACION_NIVEL_INICIAL
        self.tiempo_res = DURACION_NIVEL_INICIAL
        self.puntaje_t = 0
        self.puntaje_o = 0
        self.ponderador = 0
        self.velocidad = [VELOCIDAD_PROPS[0], VELOCIDAD_PROPS[1]]
        self.pausa = True
        self.palabra = ""

    def crear_parapentes(self):
        lista_props = []
        for i in range(4): # Crear 4 parapentes iguales
            parapente = Prop()
            parapente.numero = i + 1 # Empezar a contar desde 1
            lista_props.append(parapente)
        return lista_props
    
    def crear_props(self):

        lista_props = []

        alien5 = Prop()
        alien5.numero = 5
        lista_props.append(alien5)

        alien6 = Prop()
        alien6.numero = 6
        lista_props.append(alien6)

        alien7 = Prop()
        alien7.numero = 7
        lista_props.append(alien7)

        return lista_props

    def mover(self, prop):
        if self.pausa:
            prop.x += prop.velocidad[0]
            self.senal_mover_prop.emit(prop.x, prop.y, prop.numero)

    def explosiones(self, prop):

        if self.contador == 0:
            self.usarx = prop.x
            self.usary = prop.y

        self.enviar_explosion()

        self.timer = QTimer()
        self.timer.setInterval(700)
        self.timer.timeout.connect(self.enviar_explosion)
        self.timer.start()

        self.timer2 = QTimer()
        self.timer2.setInterval(1300)
        self.timer2.timeout.connect(self.enviar_explosion)
        self.timer2.start()

        self.timer3 = QTimer()
        self.timer3.setInterval(1900)
        self.timer3.timeout.connect(self.enviar_explosion)
        self.timer3.start()
    
    def enviar_explosion(self):

        self.contador = 1
        self.senal_boom.emit(self.usarx, self.usary, self.contador_explosion)
        self.contador_explosion +=1
    
    def tiempo_(self):
        self.timer5 = QTimer()
        self.timer5.setInterval(1000)
        self.timer5.timeout.connect(self.tiempo_actualizar)
        self.timer5.start()
    
    def tiempo_actualizar(self):
        self.tiempo_res -= 1
        self.senal_actualizar.emit()

    def mover_mira(self, mira, mira_izq):
        archivo = open("actualiza.txt","r") 
        c = 1
        for i in archivo:
            if c == 1:
                mira.izq_der = float(i)
            elif c == 2:
                mira.subir_bajar = float(i)
            elif c == 3:
                mira_izq.izq_der = float(i)
            elif c == 4:
                mira_izq.subir_bajar = float(i)
            c+= 1

        if self.pausa:
            archivo = open("actualiza.txt","r") 
            c = 1
            for i in archivo:
                if c == 1:
                    mira.izq_der = float(i)
                elif c== 2:
                    mira.subir_bajar = float(i)
                elif c == 3:
                    mira_izq.izq_der = float(i)
                elif c == 4:
                    mira_izq.subir_bajar = float(i)
                c+= 1
        archivo.close()
        self.senal_mover_mira.emit(
            mira.izq_der, mira.subir_bajar,
            mira_izq.izq_der, mira_izq.subir_bajar)

    def iniciar_pausa(self):
        self.pausa = not self.pausa
    


    
            

            






    