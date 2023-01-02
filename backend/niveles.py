# Crear clase nivel 1 con parapentes y aliados
from backend.logica_juego import Parapente

class Nivel1():
    enemigos = []
    aliados = []

    def __init__(self, posiciones_enemigos, posiciones_aliados):
        for i, xy_pos in posiciones_enemigos:
            parapente = Parapente(xy_pos, i)
            self.enemigos.append(parapente)
            
        for i, xy_pos in posiciones_aliados:
            aliado = Aliado(xy_pos, i)
            self.aliados.append(aliado)

class Nivel2():
    def __init__(self):
        self.enemigos = []
        self.aliados = []

        # TODO: Cambiar prop a perros
        for i in range(4):
            perro = Prop()
            perro.numero = i
            perro.imageUrl = "parapente{}.png".format(i+1)
            self.enemigos.append(perro)
            
        for i in range(3):
            aliado = Prop()



    