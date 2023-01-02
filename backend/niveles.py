# Crear clase nivel 1 con parapentes y aliados
from backend.logica_juego import Parapente, Planta, xy_pos, Ave

class Nivel1():
    posiciones_enemigos = [
        xy_pos(1, 100),
        xy_pos(1, 400),
        xy_pos(1, 200),
        xy_pos(1, 300),
    ]
    posiciones_plantas = [
        xy_pos(30, 200)
    ]
    posiciones_aves = [
        xy_pos(1, 400),
        xy_pos(1, 200)
    ]

    enemigos = []
    aliados = []

    def __init__(self, parent):
        for i, xy_pos in enumerate(self.posiciones_enemigos):
            parapente = Parapente(parent, xy_pos, i)
            self.enemigos.append(parapente)
            
        for i, xy_pos in enumerate(self.posiciones_plantas):
            planta = Planta(parent, xy_pos, i)
            self.aliados.append(planta)

        for i, xy_pos in enumerate(self.posiciones_aves):
            ave = Ave(parent, xy_pos, i)
            self.aliados.append(ave)
        
    def showEnemigo(self, id):
        for prop in self.enemigos:
            if prop.id == id:
                prop.show()
                prop.alive=True

    def destroyEnemigo(self, id):
        for prop in self.enemigos:
            if prop.id == id:
                prop.hide()
        
    def showAliados(self):
        for prop in self.aliados:
            prop.show()

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



    