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

import time
import sys
import os

import vue_vie
import modele_vie

# création des instances d'objet
les_ecrans = modele_vie.Ecran()

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
    time.sleep(2)
    menu_principal()

def menu_principal():
    efface_console()
    affiche = les_ecrans.ecran_menu()
    print(affiche)
    choix = input ("rentrer la lettre demandé.\nNouvelle partie aléatoire (N) \nQuitter(Q)")
    if choix == "N":
        nouvelle_partie()
    elif choix == "Q":
        quitter()

def quitter():
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()

def nouvelle_partie():
    efface_console()
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    time.sleep(5)
    menu_principal()




