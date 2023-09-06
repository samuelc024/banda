from musicos import *
from instrumentos import *
import random
class BandaAleatoria:
    def __init__(self):
        self.cantidad=random.randint(5,10)
        self.instrumentos=[Guitarra(),Maracas(),Piano(),Violin(),Trompeta(),Charrasca()]
        self.musicos=[]
        
    def ainstrumento(self):
        return random.choice(self.instrumentos)
    
    def crear_banda(self):
        for i in range(self.cantidad):
            self.musicos.append(Musico(self.ainstrumento()))
    
    def tocar_y_afinar_banda(self):
        for i in range(self.cantidad):
            self.musicos[i].afinar()  
            self.musicos[i].tocar()
            
    
                
                
                
                
                
        
if __name__ =='__main__':
    a=BandaAleatoria()
    n=a.ainstrumento()
    print(n)
