class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

# Instancier la classe Rectangle
rectangle1 = Rectangle(5, 8)

# Afficher le résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle1.aire())
