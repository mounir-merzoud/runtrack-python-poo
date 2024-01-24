class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.studentEval()

    # Assesseurs (getters)
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level

    # Mutateur (setter) pour ajouter des crédits
    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            print(f"{self.get_nom()} {self.get_prenom()} a ajouté {nombre_credits} crédits.")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"Nom : {self.__nom}")
        print(f"Prenom : {self.__prenom}")
        print(f"Id : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")

# Utilisation de la classe Student avec les nouvelles méthodes
john_doe = Student("Doe", "John", 145)

john_doe.add_credits(30)
john_doe.add_credits(60)
john_doe.add_credits(20)

# Affichage des informations de l'étudiant
john_doe.studentInfo()
