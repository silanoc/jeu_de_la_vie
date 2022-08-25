#-------------------------------------------------------------------------------
# Name:        modele vie
# Purpose:     Dans une achitecture MVC, la partie modele du jeu de la vie.
#              Contient la class Automate, qui est le moteur du jeu.
#
# Author:      silanoc
#
# Created:     08/08/2022
# Version:     1.0
#-------------------------------------------------------------------------------

import random
#---
import controleur_vie

class Automate():
    """génére une grille et les règles de bases du jeu"""

    def __init__(self, taille = (10, 10)):
        """initialise le jeu avec une grille de 10 sur 10 par défaut
        arg
        - taille (turple) : définit le nombre de lignes et de colonnes voulues.
            par defaut 10 sur 10 (10, 10)
        """
        self.taille = taille
        self.nb_ligne = taille[0]
        self.nb_colonne = taille[1]
        self.grille = [["" for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]

    def remplissage_aleatoire_a_la_creation(self):
        """créé et retourne une grille de la même taille que celle initiale, avec des 0 et 1 aléatoire dedans"""
        remplissage = [[random.randint(0,1) for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        return remplissage

    def calcul_etat_initial(self):
        """pour chaque cellule compte le nombre de voisines vivantes.
        L'écrire dans le tableau grille de calcul
        retourner ce tableau"""

        grille_de_calcul = [["" for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        for ligne in range(self.nb_ligne):
            for colonne in range(self.nb_colonne):
                # première ligne
                if ligne == 0 and colonne == 0:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne + 1] + self.grille[ligne + 1][colonne]  + self.grille[ligne + 1][colonne]
                elif ligne == 0 and colonne > 0 and colonne < self.nb_colonne -1 :
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] +  self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne == 0 and colonne == self.nb_colonne - 1:
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
                elif ligne > 0 and ligne < self.nb_ligne -1 and colonne == self.nb_colonne - 1:
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
                elif ligne == self.nb_ligne -1 and colonne == self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne - 1][colonne - 1] +  self.grille[ligne - 1][colonne]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1]
        return grille_de_calcul

    def donne_etat_final(self, valeurs_des_voisins):
        """pour chaque cellule de la grille, applique les régles du jeu écrites dans les deux dictionnaires.
        Cela permet de simplifier le style et changer les régles si on veut.
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
        """Pour enchainer deux méthodes, qui correspondent à une action pour le visuel."""
        valeurs_des_voisins = self.calcul_etat_initial()
        self.donne_etat_final(valeurs_des_voisins)
