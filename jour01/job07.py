class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe
personnage1 = Personnage(0, 0)

# Afficher la position initiale
print("Position initiale :", personnage1.position())

# Déplacer le personnage vers la droite
personnage1.droite()

# Afficher la nouvelle position
print("Nouvelle position :", personnage1.position())

# Déplacer le personnage vers le bas
personnage1.bas()

# Afficher la nouvelle position
print("Nouvelle position :", personnage1.position())
