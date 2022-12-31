from random import random, randint
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject,  QTimer
from parametros import VELOCIDAD_ALIEN, DURACION_NIVEL_INICIAL
from os import path
from random import randint
from PyQt5.QtMultimedia import QMediaPlayer, QSound
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication


class Mira(QObject):

    def __init__(self):
        super().__init__()
        self.subir_bajar = 150
        self.izq_der = 300
        self.jugador = QMediaPlayer
        self.palabra = ""

        
class Alien(QObject):
    #60,50
    #640,380

    def __init__(self):
        super().__init__()
        self.x = 1
        self.y = randint(0,330)
        self.velocidad = [VELOCIDAD_ALIEN[0],VELOCIDAD_ALIEN[1]]
        self.numero = 0
        self.espacio = [self.x, self.y , 60, 50]

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
        self.velocidad = [VELOCIDAD_ALIEN[0], VELOCIDAD_ALIEN[1]]
        self.pausa = True
        self.palabra = ""


    
    def crear_aliens(self):

        lista_aliens = []
        for niveles in range(0,self.nivel_actual):
            alien1 = Alien()
            alien1.numero = 1
            lista_aliens.append(alien1)

            alien2 = Alien()
            alien2.numero = 2
            lista_aliens.append(alien2)

            alien3 = Alien()
            alien3.numero = 3
            lista_aliens.append(alien3)

            alien4 = Alien()
            alien4.numero = 4
            lista_aliens.append(alien4)

            alien5 = Alien()
            alien5.numero = 5
            lista_aliens.append(alien5)

            alien6 = Alien()
            alien6.numero = 6
            lista_aliens.append(alien6)

            alien7 = Alien()
            alien7.numero = 7
            lista_aliens.append(alien7)

        return lista_aliens

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

        if self.pausa:
            self.pausa = False

        elif not self.pausa:
            self.pausa = True
    


    
            

            






    