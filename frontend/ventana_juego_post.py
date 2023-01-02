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

class Ventana_Juego_Post(QMainWindow):

    senal_nivel2 = pyqtSignal(int, object)

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
        self.player.setPosition(107000)
        self.player.play()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.nivel2)

        QMediaPlayer.state(self.player)

        self.setCentralWidget(self.video_widget)
        self.showFullScreen()

        # iniciar nivel 2 luego de explicacion
        self.timer.start(15000)
        

    def cerrar_juego(self):
        self.video_widget.destroy()
        self.player.stop()
        self.close()
    
    def nivel2(self):
        self.cerrar_juego()
        self.senal_nivel2.emit(1, self.juego)

    

    

    
    

