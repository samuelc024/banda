from musicos import *
import random
class BandaAleatoria:
    def __init__(self):
        self.cantidad=0
        self.instrumentos=[Guitarra(),Maracas(),Piano(),Violin(),Trompeta()]
    def cbanda(self):
        return random.randint(1,10)
    def ainstrumento(self):
        return random.choice(self.instrumentos)
    def tocar_banda(self):
        a=BandaAleatoria
        b=a.cbanda()
        for i in range(b):
            c=a.ainstrumento()
            if c==Guitarra():
                tocar.guitarra()
                
        
if __name__ =='__main__':
    a=BandaAleatoria()
    n=a.ainstrumento()
    print(n)