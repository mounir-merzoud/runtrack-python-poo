class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_compte}: {self.__nom} {self.__prenom}")

    def afficherSolde(self):
        print(f"Solde du compte: {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde: {self.__solde} €")
        else:
            print("Solde insuffisant. Opération non autorisée.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde: {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Solde insuffisant. Opération de virement non autorisée.")

# Création d'une première instance de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte=1, nom="Dupont", prenom="Jean", solde=1000)

# Appel des différentes méthodes pour vérifier le fonctionnement
compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)

# Ajout de l'attribut découvert à la première instance
compte1.__decouvert = True

# Création d'une deuxième instance à découvert
compte2 = CompteBancaire(numero_compte=2, nom="Martin", prenom="Sophie", solde=-500, decouvert=True)

# Virement du compte1 vers le compte2 pour remettre le solde à zéro
compte1.virement(compte2, 1500)

# Affichage des soldes après le virement
compte1.afficherSolde()
compte2.afficherSolde()
