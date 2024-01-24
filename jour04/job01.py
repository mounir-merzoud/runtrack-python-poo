class Personne:
    def __init__(self):
        self.__age = 14

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.get_age()} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.set_age(nouvel_age)

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.get_age()} ans")

class Professeur(Personne):
    def __init__(self, age=30, matiere_enseignee="Mathématiques"):
        super().__init__()
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une personne et d'un élève
personne1 = Personne()
eleve1 = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve1.afficherAge()

