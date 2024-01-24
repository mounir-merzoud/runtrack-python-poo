class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire pour représenter les plats commandés
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats:
            self.__plats[nom_plat] = {"prix": prix, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Plat '{nom_plat}' est déjà dans la commande.")

    def annuler_commande(self):
        self.__plats.clear()
        self.__statut_commande = "annulée"
        print("Commande annulée.")

    def __calculer_total(self):
        return sum(plat["prix"] for plat in self.__plats.values() if plat["statut"] == "en cours")

    def afficher_commande(self):
        print(f"\nCommande #{self.__numero_commande}")
        print("Plats commandés:")
        for nom_plat, details_plat in self.__plats.items():
            print(f"{nom_plat}: {details_plat['prix']} € - Statut: {details_plat['statut']}")
        print(f"Total à payer : {self.__calculer_total()} € (TVA incluse)")
        print(f"Statut de la commande : {self.__statut_commande}")

    def calculer_tva(self):
        total_tva = sum(details_plat["prix"] * 0.20 for details_plat in self.__plats.values() if details_plat["statut"] == "en cours")
        return total_tva

# Exemple d'utilisation de la classe Commande
commande1 = Commande(1)

commande1.ajouter_plat("Pizza", 15)
commande1.ajouter_plat("Salade", 8)

commande1.afficher_commande()

commande1.ajouter_plat("Burger", 12)
commande1.afficher_commande()

commande1.annuler_commande()
commande1.afficher_commande()

print(f"TVA à payer pour la commande : {commande1.calculer_tva()} €")
