class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'âge de l'animal : {self.age} ans")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")

# Instanciation d'un objet Animal
monAnimal = Animal()

# Affichage de l'âge initial de l'animal
monAnimal.afficherAge()

# Faire vieillir l'animal
monAnimal.vieillir()

# Affichage de l'âge après vieillissement
monAnimal.afficherAge()

# Nommer l'animal
monAnimal.nommer("Luna")
