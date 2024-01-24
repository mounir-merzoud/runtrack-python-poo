import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, ou 3): "))

    def lancerJeu(self):
        self.choisirNiveau()

        points_de_vie_joueur = self.niveau * 50
        points_de_vie_ennemi = self.niveau * 30

        joueur = Personnage("Joueur", points_de_vie_joueur)
        ennemi = Personnage("Ennemi", points_de_vie_ennemi)

        print(f"\nNouvelle partie - Niveau {self.niveau}")
        print(f"{joueur.nom} a {joueur.vie} points de vie.")
        print(f"{ennemi.nom} a {ennemi.vie} points de vie.")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            print(f"{joueur.nom} a {joueur.vie} points de vie restants.")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie restants.\n")

        self.verifierResultat(joueur, ennemi)

    def verifierResultat(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("Vous avez perdu. L'ennemi a gagné.")
        else:
            print("Félicitations ! Vous avez vaincu l'ennemi.")

# Créer une instance de Jeu
jeu = Jeu()

# Lancer le jeu
jeu.lancerJeu()
