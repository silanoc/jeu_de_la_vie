#-------------------------------------------------------------------------------
# Name:        Jeu de la vie
# Purpose:     Démonstrateur simple du jeu de la vie. PAs d'interface utilisateur,
#              les paramètres sont à définir dans le programme.
#              sert à tester la logique de base pour une version avec interface.
#
# Author:      silanoc
# Created:     07/08/2022
# Version:     1.0
#-------------------------------------------------------------------------------
import random
import time

class Automate():
    """génére une grille et les regles de bases du jeu"""

    def __init__(self, taille = (10, 10)):
        """initialise le jeu avec une grille de 10 sur 10 par defaut
        arg
        - taille (turple) : donne le nombre de lignes et de colonnes.
            par defaut 10 sur 10 (10, 10)
        """
        self.t_debut_init = time.time()
        self.taille = taille
        self.nb_ligne = taille[0]
        self.nb_colonne = taille[1]
        self.grille = [["" for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        self.t_fin_init = time.time()
        self.t_fin_calcul_etat_initial = 0
        self.t_debut_calcul_etat_initial = 0

    def remplissage_aleatoire_a_la_creation(self):
        """créé et retourne une grille de la même taille que celle initiale, avec des 0 et 1 aléatoire dedans"""
        remplissage = [[random.randint(0,1) for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        return remplissage

    def affichage_grille(self):
        """affiche dans la consolle la grille
        pour plus de lisibilité, espace vide si 0 et X si vivant"""

        for ligne in range(self.nb_ligne):
            affiche = ""
            for colonne in range(self.nb_colonne):
                if self.grille[ligne][colonne] == 0:
                    affiche += " "
                else:
                    affiche += "X"
            print(affiche)

    def calcul_etat_initial(self):
        """pour chaque cellule compte le nombre de voisin vivant.
        L'écrire dans le tableau grille de calcul
        retourner ce tableau"""
        self.t_debut_calcul_etat_initial = time.time()
        grille_de_calcul = [["" for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        for ligne in range(self.nb_ligne):
            for colonne in range(self.nb_colonne):
                # première ligne
                if ligne == 0 and colonne == 0:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne + 1] + self.grille[ligne + 1][colonne]  + self.grille[ligne + 1][colonne]
                elif ligne == 0 and colonne > 0 and colonne < self.nb_colonne -1 :
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] +  self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne == 0 and colonne == self.nb_colonne -1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne - 1] + self.grille[ligne + 1][colonne -1]  + self.grille[ligne + 1][colonne]
                # toutes les lignes sauf première et dernière
                elif ligne > 0 and ligne < self.nb_ligne -1 and colonne == 0:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne] +  self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne > 0 and ligne < self.nb_ligne -1 and colonne > 0 and colonne < self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne - 1] +  self.grille[ligne - 1][colonne] +  self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] +  self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne > 0 and ligne < self.nb_ligne -1 and colonne == self.nb_colonne -1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne - 1] +  self.grille[ligne - 1][colonne]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] +  self.grille[ligne + 1][colonne]
                # dernière ligne
                elif ligne == self.nb_ligne -1 and colonne == 0:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne] +  self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne + 1]
                elif ligne == self.nb_ligne -1 and colonne > 0 and colonne < self.nb_colonne -1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne - 1] +  self.grille[ligne - 1][colonne] +  self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                elif ligne == self.nb_ligne -1 and colonne == self.nb_colonne -1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne - 1] +  self.grille[ligne - 1][colonne]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1]
        self.t_fin_calcul_etat_initial = time.time()
        return grille_de_calcul

    def donne_etat_final(self, valeurs_des_voisins):
        """pour chaque cellule de la grille, applique les régles du jeu écritent dans les deux dictionnaires.
        Ecrit directement dans la grille le nouvel état."""

        dico_si_vivant = {0:0, 1:0, 2:1, 3:1, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        dico_si_mort =  {0:0, 1:0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

        for ligne in range(self.nb_ligne):
            for colonne in range(self.nb_colonne):
                if self.grille[ligne][colonne] == 0:
                    self.grille[ligne][colonne] = dico_si_mort[valeurs_des_voisins[ligne][colonne]]
                elif self.grille[ligne][colonne] == 1:
                    self.grille[ligne][colonne] = dico_si_vivant[valeurs_des_voisins[ligne][colonne]]

    def genere_nouvelle_generation(self):

        valeurs_des_voisins = self.calcul_etat_initial()
        self.donne_etat_final(valeurs_des_voisins)
        self.tf = time.time()


def main(nb_generation = 10):
    vie = Automate((15, 15))
    t = vie.t_fin_init - vie.t_debut_init
    print("temps initialisation : ",t)
    print("---generation initiale-------")
    vie.grille = vie.remplissage_aleatoire_a_la_creation()
    vie.affichage_grille()
    for i in range(1, nb_generation + 1):
        print(f"---generation {i}-------")
        t =  vie.t_fin_calcul_etat_initial - vie.t_debut_calcul_etat_initial
        print("temsp calcul etat initial :", t)
        ti = time.time()
        vie.genere_nouvelle_generation()
        tf = time.time()
        print(tf - ti)
        vie.affichage_grille()

if __name__ == '__main__':
    main(1)
