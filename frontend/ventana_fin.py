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

class Ventana_Fin(QMainWindow):

    #senal_enviar_jugar = pyqtSignal(int, object)

    def __init__(self):
        super().__init__()
        #self.initUI()

    def mostrar(self, espacio, juego):
        self.initUI(espacio, juego)

    def initUI(self, espacio, juego):
        # Crear el widget QVideoWidget y establecerlo como el visor de video del reproductor
        self.video_widget = QVideoWidget(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("BASEJUEGO.mp4")))
        self.player.setPosition(183000)
        self.player.play()

        self.boton_salir = QPushButton("",self)
        self.boton_salir.setGeometry(700, 450, 500,200 )
        self.boton_salir.setText("Salir")
        #self.boton_jugar.setIcon(QIcon("../programa/data/boton_jugar.png"))
        #self.boton_salir.setIconSize(1 * QSize(self.boton_salir.width(), self.boton_salir.height()))
        self.boton_salir.clicked.connect(self.cerrar_juego)
        self.boton_salir.setVisible(False)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.boton)

        QMediaPlayer.state(self.player)

        self.setCentralWidget(self.video_widget)
        self.showFullScreen()

        # Inicia el temporizador para que se ejecute la función después de 3000 milisegundos (3 segundos)
        self.timer.start(120000)
        

    def cerrar_juego(self):
        self.video_widget.destroy()
        self.player.stop()
        self.close()
    
    def boton(self):
        self.boton_salir.setVisible(True)

    

    

    
    

