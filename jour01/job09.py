class Produit:
    def __init__(self, nom, prixHT, tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        print(f"Informations du produit {self.nom}:")
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT} euros")
        print(f"TVA : {self.tva}%")
        print(f"Prix TTC : {self.calculerPrixTTC()} euros")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def retournerNom(self):
        return self.nom

    def retournerPrixHT(self):
        return self.prixHT

    def retournerTVA(self):
        return self.tva

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Smartphone", 500, 19)

# Affichage des informations initiales
produit1.afficher()
print("\n")
produit2.afficher()

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Laptop")
produit1.modifierPrixHT(900)
produit2.modifierNom("Téléphone")
produit2.modifierPrixHT(600)

# Affichage des informations modifiées
print("\nAprès modification :")
produit1.afficher()
print("\n")
produit2.afficher()
