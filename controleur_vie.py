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

import vue_vie
import modele_vie

# création des instances d'objet
les_ecrans = modele_vie.Ecran()

def demarer_jeu():
    affiche = les_ecrans.ecran_ouverture_jeu()
    print(affiche)
    time.sleep(2)
    menu_principal()

def menu_principal():
    affiche = les_ecrans.ecran_menu()
    print(affiche)
    choix = input ("rentrer la lettre demandé.\nNouvelle partie aléatoire (N) \nQuitter(Q)")
    if choix == "N":
        nouvelle_partie()
    elif choix == "Q":
        quitter()

def quitter():
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()

def nouvelle_partie():
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    time.sleep(5)
    menu_principal()




