class Instrumento:
    def afinar(self):
        pass
    def tocar(self):
        pass
    class Maracas(Instrumento):
        def afinar(self):
            print("Las maracas no necesitan ser afinadas y ")
        def tocar(self):
            print("se estan tocando las maracas")
    class Piano(Instrumento):
        def afinar(self):
            print("El piano no necesita ser afinado")
        def tocar(self):
            print("se estan tocando el piano")
    class Guitarra(Instrumento):
        def afinar(self):
            print("La guitarra esta afinada y ")
        def tocar(self):
            print("se esta tocando la guitarra")
    class Trompeta(Instrumento):
        def afinar(self):
            print("La tromepta esta afinada y ")
        def tocar(self):
            print("se esta tocando la tompeta")
    

if __name__ =='__main__':
    u = Instrumento()
    u.afinar()

