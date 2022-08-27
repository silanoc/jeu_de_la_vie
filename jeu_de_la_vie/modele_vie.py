#! /usr/bin/env python3
# coding: utf-8

"""Dans une achitecture MVC, la partie modele du jeu de la vie.
Contient la class Automate, qui est le moteur du jeu.
"""

import random
from typing import Tuple
import jeu_de_la_vie.controleur_vie as controleur_vie


class Automate():
    """Objet de base du jeu.
    Basé autour d'une grille (liste de liste).
    Posséde les méthodes pour se remplir, regarder l'état des cellules voisines et générer le nouvel état.
    
    Initialise le jeu avec une grille de 10 sur 10 par défaut.
    
    Toutes les cellules sont initialisé avec 99 (valeur absurde).
    
    Permet d'avoir self.grille d'utilisable pour tout le reste.
        
    :param turple taille: définit le nombre de lignes et de colonnes voulues. Par défaut (10, 10).
    """

    def __init__(self, taille: Tuple[int, int] = (10, 10)) -> None:

        self.taille: Tuple[int, int] = taille
        self.nb_ligne:int = taille[0]
        self.nb_colonne: int = taille[1]
        self.grille: list[list[int]] = [[99 for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]

    def remplissage_aleatoire_a_la_creation(self) -> list[list[int]]:
        """Créé et retourne une grille de la même taille que celle initiale, avec des 0 et 1 aléatoire dedans.
        
        :returns: remplissage (liste de liste) dont toutes les valeurs sont des 0 ou des 1.
        :rtype: list
        """
        remplissage: list[list[int]] = [[random.randint(0,1) for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        return remplissage

    def calcul_etat_initial(self) -> list[list[int]]:
        """Pour chaque cellule de self.grille compte le nombre de voisines vivantes. 
        
        Incrémente dans le tableau grille_de_calcul la valeur de l'état de chacune des 8 voisines de self.grille.
        
        :returns: grille_de_calcul (liste de liste), valeurs allant de 0 à 8.
        :rtype: list
        """
        grille_de_calcul: list[list[int]] = [[0 for i in range(self.nb_colonne)] for j in range(self.nb_ligne)]
        for ligne in range(self.nb_ligne):
            for colonne in range(self.nb_colonne):
                # première ligne
                if ligne == 0 and colonne == 0:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne + 1] + self.grille[ligne + 1][colonne]  + self.grille[ligne + 1][colonne]
                elif ligne == 0 and colonne > 0 and colonne < self.nb_colonne -1 :
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] + self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne == 0 and colonne == self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] = self.grille[ligne][colonne - 1] + self.grille[ligne + 1][colonne -1]  + self.grille[ligne + 1][colonne]
                # toutes les lignes sauf première et dernière
                elif ligne > 0 and ligne < self.nb_ligne - 1 and colonne == 0:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne] + self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne > 0 and ligne < self.nb_ligne - 1 and colonne > 0 and colonne < self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne - 1] + self.grille[ligne - 1][colonne] + self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] +  self.grille[ligne + 1][colonne] + self.grille[ligne + 1][colonne + 1]
                elif ligne > 0 and ligne < self.nb_ligne - 1 and colonne == self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne - 1] + self.grille[ligne - 1][colonne]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne + 1][colonne - 1] + self.grille[ligne + 1][colonne]
                # dernière ligne
                elif ligne == self.nb_ligne - 1 and colonne == 0:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne] +  self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne + 1]
                elif ligne == self.nb_ligne - 1 and colonne > 0 and colonne < self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne - 1] + self.grille[ligne - 1][colonne] + self.grille[ligne - 1][colonne + 1]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1] + self.grille[ligne][colonne + 1]
                elif ligne == self.nb_ligne - 1 and colonne == self.nb_colonne - 1:
                    grille_de_calcul[ligne][colonne] += self.grille[ligne - 1][colonne - 1] + self.grille[ligne - 1][colonne]
                    grille_de_calcul[ligne][colonne] += self.grille[ligne][colonne - 1]
        return grille_de_calcul

    def donne_etat_final(self, valeurs_des_voisins: list[list[int]]) -> None:
        """Pour chaque cellule de self.grille defini son nouvel état (0 ou 1).
        
        Applique les régles du jeu écrites dans les deux dictionnaires.
        Cela permet de simplifier le style et changer les régles si on veut.
        
        Ecrit directement dans la self.grille le nouvel état.
        
        :param list valeurs_des_voisines: (liste_de_liste), valeurs entre 0 et 8, calculées dans calcul_etat_initial().
        """

        dico_si_vivant: dict[int, int] = {0 : 0, 1 : 0, 2 : 1, 3 : 1, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
        dico_si_mort: dict[int, int] = {0 : 0, 1 : 0, 2 : 0, 3 : 1, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}

        for ligne in range(self.nb_ligne):
            for colonne in range(self.nb_colonne):
                if self.grille[ligne][colonne] == 0:
                    self.grille[ligne][colonne] = dico_si_mort[valeurs_des_voisins[ligne][colonne]]
                elif self.grille[ligne][colonne] == 1:
                    self.grille[ligne][colonne] = dico_si_vivant[valeurs_des_voisins[ligne][colonne]]

    def genere_nouvelle_generation(self) -> None:
        """Calcul d'une génération du jeu pour toutes les cellules. Nécessaire pour afficher dans la console.
        
        Enchaine les deux méthodes afin de calculer le nouvel état de chaque cellule de self.grille  
        """
        valeurs_des_voisins: list[list[int]] = self.calcul_etat_initial()
        self.donne_etat_final(valeurs_des_voisins)