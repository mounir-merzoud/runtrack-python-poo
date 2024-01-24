import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon {self.rayon}")

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations, circonférence, diamètre et aire pour chaque cercle
cercle1.afficherInfos()
print("Circonférence :", cercle1.circonférence())
print("Diamètre :", cercle1.diametre())
print("Aire :", cercle1.aire())

print("\n")

cercle2.afficherInfos()
print("Circonférence :", cercle2.circonférence())
print("Diamètre :", cercle2.diametre())
print("Aire :", cercle2.aire())
