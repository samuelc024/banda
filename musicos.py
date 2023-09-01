from piano import Piano 
from guitarra import Guitarra 
from maracas import Maracas 
from trompeta import Trompeta 
from violin import Violin 
import random
class Musico:
    def __init__(self,instrumento):
        self.instrumento=instrumento
    def tocar(self):
        self.instrumento.tocar()
    def afinar(self):
        self.instrumento.afinar()
    
