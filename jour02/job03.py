class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    # Nouvel assesseur pour l'attribut disponible
    def est_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Nouvelle méthode de vérification de disponibilité
    def verification(self):
        return self.__disponible

    # Nouvelle méthode d'emprunt
    def emprunter(self):
        if self.verification():
            print("Emprunt du livre en cours.")
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Nouvelle méthode de rendu
    def rendre(self):
        if not self.verification():
            print("Rendu du livre en cours.")
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")

# Exemple d'utilisation
mon_livre = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1000)

# Vérification de la disponibilité du livre
print("Le livre est disponible :", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Vérification de la disponibilité après l'emprunt
print("Le livre est disponible :", mon_livre.verification())

# Rendu du livre
mon_livre.rendre()

# Vérification de la disponibilité après le rendu
print("Le livre est disponible :", mon_livre.verification())
