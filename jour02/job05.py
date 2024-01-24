class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # Initialisé à 50 par défaut

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def set_en_marche(self, nouvel_etat):
        self.__en_marche = nouvel_etat

    def set_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir > 5

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein():
            print("La voiture démarre.")
            self.__en_marche = True
        else:
            print("La voiture ne peut pas démarrer. Le réservoir est trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        print("La voiture s'arrête.")
        self.__en_marche = False

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "CHR", 2020, 30000)

# Affichage des informations initiales
print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())
print("Réservoir :", ma_voiture.get_reservoir())

# Démarrage de la voiture
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()
