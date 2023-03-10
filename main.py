
from PyQt5.QtWidgets import QApplication
import sys
from frontend.ventana_inicio import Ventana_Inicio
from frontend.ventana_juego import Ventana_Juego
from frontend.ventana_juego2 import Ventana_Juego2
from backend.logica_juego import Juego, Mira
from PyQt5 import  QtWidgets
from frontend.ventana_postjuego import Ventana_Postjuego


app = QApplication([])


if __name__ == '__main__':
    # Instanciación de ventanas
    ventana_inicio = Ventana_Inicio()
    ventana_juego = Ventana_Juego()
    ventana_juego2 = Ventana_Juego2()
    ventana_postjuego = Ventana_Postjuego()


    # Instanciación de lógica
    logica_mira = Mira()
    logica_juego = Juego()

    # Conexiones de señales
    ventana_inicio.senal_enviar_jugar.connect(ventana_juego.mostrar)    

    ventana_juego.senal_tecla.connect(logica_juego.mover_mira)
    logica_juego.senal_mover_mira.connect(ventana_juego.actualizar_movimiento)

    logica_juego.senal_disparo.connect(ventana_juego.disparo)

    ventana_juego.senal_postjuego.connect(ventana_postjuego.mostrar)
    ventana_postjuego.senal_salir.connect(ventana_inicio.show)

    ventana_postjuego.senal_siguiente_nivel.connect(ventana_juego.mostrar)
    ventana_juego.senal_explosion.connect(logica_juego.explosiones)
    logica_juego.senal_boom.connect(ventana_juego.explosion)

    logica_juego.senal_actualizar.connect(ventana_juego.tiempo_actualizar)

    #Mostrar la ventana, aca comienza el programa
    ventana_inicio.show()
    #ventana_juego.mostrar(1, logica_juego)
    sys.exit(app.exec_())