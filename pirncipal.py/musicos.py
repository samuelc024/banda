from instrumentos import *
import random
class Musico:
    def __init__(self,instrumento):
        self.instrumento=instrumento
    def tocar(self):
        self.instrumento.tocar()
    def afinar(self):
        self.instrumento.afinar()
    
