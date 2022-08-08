#-------------------------------------------------------------------------------
# Name:        controleur vie
# Purpose:
#
# Author:      Gabriel-le
#
# Created:     08/08/2022
# Copyright:   (c) Gabriel-le 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import vue_vie
import modele_vie

def gestion_choix_menu_principal(choix):
    if choix == "N":
        grille_de_jeu = creer_une_grille_initale()
        affichage = grille_de_jeu.grille
        vue_vie.nouvelle_partie(affichage)
    elif choix == "Q":
        vue_vie.quitter()

def creer_une_grille_initale():
    grille_de_jeu = modele_vie.Automate()
    grille_de_jeu.grille = grille_de_jeu.remplissage_aleatoire_a_la_creation()
    return grille_de_jeu








