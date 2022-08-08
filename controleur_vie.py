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

#global grille_de_jeu
#grille_de_jeu = modele_vie.Automate((1,1))

def creer_une_grille_initale():
    grille_de_jeu = modele_vie.Automate((5,5))
    grille_de_jeu.grille = grille_de_jeu.remplissage_aleatoire_a_la_creation()
    return grille_de_jeu

def gestion_choix_menu_principal(choix):
    if choix == "N":
        grille_de_jeu = creer_une_grille_initale()
        affichage = grille_de_jeu.grille
        vue_vie.nouvelle_partie(affichage, grille_de_jeu)
    elif choix == "Q":
        vue_vie.quitter()

def gestion_demande_nouveau_tour(choix, grille, grille_de_jeu):
    if choix == "n":
        vue_vie.menu_principal()
    elif choix == "O":
        grille_de_jeu.genere_nouvelle_generation()
        grille = grille_de_jeu.grille
        vue_vie.affiche_une_grille(grille, grille_de_jeu)







