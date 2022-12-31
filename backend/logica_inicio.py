from PyQt5.QtCore import QObject, pyqtSignal

class Logica_Inicio(QObject):

    def __init__(self):
        super().__init__()

    def usuario (self, nombre):
        return nombre.isalnum()

        
            


    
