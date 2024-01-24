class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def allerEnCours(self):
        print("Je vais en cours.")

    def bonjour(self):
        print(f"Bonjour, je suis l'élève {self.nom} et j'ai {self.age} ans.")

        # Redéfinir l'âge de l'élève à 15 ans
        self.age = 15
        print(f"Mon âge a été mis à jour : {self.age} ans.")


class Professeur(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def enseigner(self):
        print(f"Bonjour, je suis le professeur {self.nom}. Le cours commence.")

# Créer un élève
eleve1 = Eleve("Alice", 14)

# Dire bonjour à l'élève et aller en cours
eleve1.bonjour()
eleve1.allerEnCours()

# Créer un professeur
professeur1 = Professeur("M. Dupont", 40)

# Dire bonjour au professeur et commencer le cours
professeur1.bonjour()
professeur1.enseigner()
