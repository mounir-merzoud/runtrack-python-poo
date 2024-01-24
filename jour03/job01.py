class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom
        self._nombre_habitants = nombre_habitants 

        """Attribut privé avec un underscore"""

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def ajouter_population(self):
        self._nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouter_population(self):
        self.ville.ajouter_population()


# Création de l'objet Ville "Paris" avec 1 000 000 habitants
paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à {paris.nom}: {paris.get_nombre_habitants()}")

# Création de l'objet Ville "Marseille" avec 861 635 habitants
marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants à {marseille.nom}: {marseille.get_nombre_habitants()}")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout des personnes à la population des villes
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à {paris.nom} après l'arrivée de John et Myrtille: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {marseille.nom} après l'arrivée de Chloé: {marseille.get_nombre_habitants()}")
