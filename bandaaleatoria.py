from musicos import *
import random
class BandaAleatoria:
    def __init__(self):
        self.guitarra=Guitarra()
        self.maracas=Maracas()
        self.flauta=Flauta()
        self.violin=Violin()
        self.piano=Piano()
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
                print(self.guitarra.tocar())
            elif c==Maracas():
                print(self.maracas.tocar())
            elif c==Piano():
                print(self.piano.tocar())
            elif c==Violin():
                print(self.violon.tocar())
            elif c==Maracas():
                print(self.maracas.tocar())
                
                
                
                
                
        
if __name__ =='__main__':
    a=BandaAleatoria()
    n=a.ainstrumento()
    print(n)