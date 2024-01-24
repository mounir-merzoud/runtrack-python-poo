class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur  # Attribut privé
        self._largeur = largeur    # Attribut privé

    # Assesseurs et mutateurs
    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur = largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur  # Attribut privé

    # Assesseur et mutateur pour la hauteur
    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur

# Instancier la classe Rectangle
rectangle1 = Rectangle(5, 8)

# Afficher le périmètre et la surface du rectangle
print("Périmètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())

# Instancier la classe Parallelepipede
parallelepipede1 = Parallelepipede(3, 4, 6)

# Afficher le volume du parallélépipède
print("Volume du parallélépipède :", parallelepipede1.volume())
