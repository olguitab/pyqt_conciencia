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

class Ventana_Juego2_Post(QMainWindow):

    senal_nivel3 = pyqtSignal(int, object)

    def __init__(self):
        super().__init__()
        #self.initUI()


    def mostrar(self, espacio, juego):
        self.juego = juego
        # Crear el widget QVideoWidget y establecerlo como el visor de video del reproductor
        self.video_widget = QVideoWidget(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("BASEJUEGO.mp4")))
        self.player.setPosition(137000)
        self.player.play()
        
        self.timer = QTimer()

        QMediaPlayer.state(self.player)

        self.setCentralWidget(self.video_widget)
        self.showFullScreen()

        # iniciar nivel 2 luego de explicacion
        self.timer.singleShot(20000, self.nivel3)
        

    def cerrar_juego(self):
        self.video_widget.destroy()
        self.player.stop()
        self.close()
    
    def nivel3(self):
        self.senal_nivel3.emit(1, self.juego)
        self.cerrar_juego()

    

    

    
    

