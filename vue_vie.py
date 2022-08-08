#-------------------------------------------------------------------------------
# Name:        vue vie
# Purpose:
#
# Author:      Gabriel-le
#
# Created:     08/08/2022
# Copyright:   (c) Gabriel-le 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import sys
import os
#---
import controleur_vie

class Ecran():
    def ecran_ouverture_jeu(self):
        affiche = """Bienvenu sur mon programme

        Jeu de la vie

        by silanoc - aout 2022"""

        return affiche

    def ecran_menu(self):
        affiche = "Vous avez plusieurs choix"
        return affiche

    def ecran_quitter(self):
        affiche = "Merci d'avoir utilisé ce programme. A une prochaine occasion."
        return affiche

    def ecran_debut_partie(self):
        affiche = "partie en cours"
        return affiche

#-------------------------------------------------------------------------------

les_ecrans = Ecran()

def efface_console():
	"""pour nettoyer la console entre chaque vue, et avoir quelque chose de propre"""
	if sys.platform.startswith("win"): #si windows
		os.system("cls")
	else :
		os.system("clear")

def demarer_jeu():
    efface_console()
    affiche = les_ecrans.ecran_ouverture_jeu()
    print(affiche)
    time.sleep(1)
    menu_principal()

def menu_principal():
    efface_console()
    affiche = les_ecrans.ecran_menu()
    print(affiche)
    choix = input ("rentrer la lettre demandée.\nNouvelle partie aléatoire (N) \nQuitter(Q)")
    controleur_vie.gestion_choix_menu_principal(choix)

def nouvelle_partie(grille, grille_de_jeu):
    efface_console()
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    time.sleep(1)
    affiche_une_grille(grille, grille_de_jeu)

def affiche_une_grille(grille, grille_de_jeu):
    for ligne in grille:
        print(ligne)
    time.sleep(2)
    choix = input("encore un tour O/n")
    controleur_vie.gestion_demande_nouveau_tour(choix, grille, grille_de_jeu)


def quitter():
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()