import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

# Instancier la classe Rectangle
rectangle1 = Rectangle(5, 8)

# Afficher le résultat de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle1.aire())

# Instancier la classe Cercle
cercle1 = Cercle(3)

# Afficher le résultat de la méthode aire de la classe Cercle
print("Aire du cercle :", cercle1.aire())
