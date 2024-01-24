class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Prix: {self.prix} euros")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

# Instancier un objet Voiture
voiture1 = Voiture(marque="Toyota", modele="Corolla", annee=2022, prix=25000)

# Appeler la méthode informationsVehicule de la classe Voiture
voiture1.informationsVehicule()
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

# Instancier un objet Moto
moto1 = Moto(marque="Harley-Davidson", modele="Sportster", annee=2022, prix=12000)

# Appeler la méthode informationsVehicule de la classe Moto
moto1.informationsVehicule()
