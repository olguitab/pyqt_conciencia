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
from backend.niveles import Nivel1
from backend.logica_juego import Juego

class Ventana_Inicio(QMainWindow):

    senal_enviar_jugar = pyqtSignal(object, object)

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:rgba(0,255,0,0%);")
        self.initUI()

    def initUI(self):
        # Crear el widget QVideoWidget y establecerlo como el visor de video del reproductor
        self.video_widget = QVideoWidget(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video_widget)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("BASEJUEGO.mp4")))
        self.player.play()
        
        self.boton_jugar = QPushButton("",self)
        self.boton_jugar.setGeometry(700, 450, 500,200 )
        self.boton_jugar.setIcon(QIcon("../programa/data/boton_jugar.png"))
        self.boton_jugar.setIconSize(1 * QSize(self.boton_jugar.width(), self.boton_jugar.height()))
        self.boton_jugar.clicked.connect(self.abrir_juego)
        #self.boton_jugar.setFixedSize(136, 64)

        self.timer = QTimer()
        self.timer.timeout.connect(self.boton)
        # Inicia el temporizador para que se ejecute la función después de 3000 milisegundos (3 segundos)

        QMediaPlayer.state(self.player)
        self.boton_jugar.setVisible(False)

        self.setCentralWidget(self.video_widget)
        self.showFullScreen()

        self.timer.start(55000)
        # Abre el video

    def abrir_juego(self):
        juego = Juego()
        nivel = Nivel1()
        self.senal_enviar_jugar.emit(nivel,juego)
        self.video_widget.destroy()
        self.player.stop()
        self.close()
    
    def boton(self):
        self.boton_jugar.setVisible(True)

    

    

    
    

