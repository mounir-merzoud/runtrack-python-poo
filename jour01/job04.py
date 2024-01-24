class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Bonjour, je suis {self.prenom} {self.nom}"

"""Instanciation de plusieurs personnes"""
personne1 = Personne("Dupond", "Jean")
personne2 = Personne("Doe", "John")


"""Appel à la méthode SePresenter pour chaque personne"""
resultat1 = personne1.SePresenter()
resultat2 = personne2.SePresenter()


# Affichage des résultats
print(resultat1)
print(resultat2)

