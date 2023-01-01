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

class Nivel2():

    def __init__(self):
        self.enemigos = []
        self.aliados = []

        for i in range(4): # Crear 4 perros
            # TODO: Agregar perros a los enemigos
            pass

        # TODO: Agregar aliados

        

