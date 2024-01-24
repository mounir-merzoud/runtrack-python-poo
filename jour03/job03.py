class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"

    def afficherListe(self):
        return [t.titre for t in self.taches]

    def filterListe(self, statut):
        return [t.titre for t in self.taches if t.statut == statut]


# Tester le code
# Créer des instances de Tache
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 5")

# Créer une instance de ListeDeTaches
liste_de_taches = ListeDeTaches()

# Ajouter des tâches à la liste
liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)

# Afficher la liste initiale
print("Liste initiale:", liste_de_taches.afficherListe())

# Marquer une tâche comme terminée
liste_de_taches.marquerCommeFinie("Faire les courses")

# Afficher la liste mise à jour
print("Liste après marquerCommeFinie:", liste_de_taches.afficherListe())

# Filtrer les tâches à faire
taches_a_faire = liste_de_taches.filterListe("à faire")
print("Tâches à faire:", taches_a_faire)

# Supprimer une tâche
liste_de_taches.supprimerTache("Réviser pour l'examen")

# Afficher la liste mise à jour
print("Liste après suppression de tâche:", liste_de_taches.afficherListe())
