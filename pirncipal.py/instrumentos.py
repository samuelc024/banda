class Instrumento:
    def afinar(self):
        pass
    def tocar(self):
        pass
class Maracas(Instrumento):
    def afinar(self):
        print("-Las maracas no necesitan ser afinadas,")
    def tocar(self):
        print("se estan tocando las maracas \n")
class Piano(Instrumento):
    def afinar(self):
        print("-El piano no necesita ser afinado,")
    def tocar(self):
        print("se estan tocando el piano \n")
class Guitarra(Instrumento):
    def afinar(self):
        print("-La guitarra esta afinada,")
    def tocar(self):
        print("se esta tocando la guitarra \n")
class Trompeta(Instrumento):
    def afinar(self):
        print("-La tromepta esta afinada,")
    def tocar(self):
        print("se esta tocando la tompeta \n")
class Violin(Instrumento):
    def afinar(self):
        print("-El violin esta afinado,")
    def tocar(self):
        print("se esta tocando el violin \n")
class Charrasca(Instrumento):
    def afinar(self):
        print("-La charrasca no necesita ser afinada,")
    def tocar(self):
        print("se esta tocando la charrasca \n")


if __name__ =='__main__':
    u = Instrumento()
    u.afinar()

