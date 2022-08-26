#-------------------------------------------------------------------------------
# Name:        controleur vie
# Purpose:     dans une architecture MVC, contrôeleur du jeu de la vie.
#
# Author:      silanoc
#
# Created:     08/08/2022
# Version :    1.1
#-------------------------------------------------------------------------------

import jeu_de_la_vie.vue_vie as vue_vie
import jeu_de_la_vie.modele_vie as modele_vie

def creer_une_grille_initale(ligne, colonne):
    grille_de_jeu = modele_vie.Automate((ligne,colonne))
    grille_de_jeu.grille = grille_de_jeu.remplissage_aleatoire_a_la_creation()
    vue_vie.nouvelle_partie(grille_de_jeu.grille, grille_de_jeu)

def gestion_choix_menu_principal(choix):
    if choix == "Nouvelle partie aléatoire":
        vue_vie.choix_taille_grille()
        #vue_vie.nouvelle_partie(affichage, grille_de_jeu)
    elif choix == "Quitter":
        vue_vie.quitter()

def gestion_choix_taille(ligne, colonne):
    grille_de_jeu = creer_une_grille_initale(ligne, colonne)

def gestion_demande_nouveau_tour(choix, grille, grille_de_jeu):
    if choix == False:
        vue_vie.menu_principal()
    elif choix == True:
        grille_de_jeu.genere_nouvelle_generation()
        grille = grille_de_jeu.grille
        vue_vie.affiche_une_grille(grille, grille_de_jeu)







