import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()

    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_total_points(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur.isdigit():
                total += int(carte.valeur)
            elif carte.valeur in ['J', 'Q', 'K']:
                total += 10
            elif carte.valeur == 'A':
                total += 11  # On suppose temporairement que l'As vaut toujours 11
                as_count += 1

        # Gérer les As si le total dépasse 21
        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total

    def distribuer_cartes(self, nombre_cartes=2):
        main = []
        for _ in range(nombre_cartes):
            main.append(self.paquet.pop())
        return main

# Exemple d'utilisation
jeu_blackjack = Jeu()

main_joueur = jeu_blackjack.distribuer_cartes()
main_croupier = jeu_blackjack.distribuer_cartes()

print("Main du joueur:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

print("\nMain du croupier:")
print(f"{main_croupier[0].valeur} de {main_croupier[0].couleur} (carte face visible)")

total_joueur = jeu_blackjack.calculer_total_points(main_joueur)
total_croupier = jeu_blackjack.calculer_total_points(main_croupier)

print(f"\nTotal des points du joueur : {total_joueur}")
print(f"Total des points du croupier : {total_croupier}")
