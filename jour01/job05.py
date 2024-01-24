class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Instanciation d'un point avec des coordonnées initiales
point1 = Point(2, 3)

# Appel des méthodes pour afficher les coordonnées
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

# Changer les coordonnées du point
point1.changerX(5)
point1.changerY(7)

# Afficher les nouvelles coordonnées
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
