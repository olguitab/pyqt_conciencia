# Crear clase nivel 1 con parapentes y aliados
from backend.logica_juego import Prop

class Nivel1():
    def __init__(self):
        self.enemigos = []
        self.aliados = []

        for i in range(4):
            parapente = Prop()
            parapente.numero = i
            parapente.imageUrl = "parapente{}.png".format(i+1)
            self.enemigos.append(parapente)
            
        for i in range(3):
            aliado = Prop()

    