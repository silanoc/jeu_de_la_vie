#-------------------------------------------------------------------------------
# Name:        vue vie
# Purpose:     dans le modèle MVC le gestionnaire de vue.
#
# Author:      silanoc
#
# Created:     08/08/2022
# Version :    1.0
#-------------------------------------------------------------------------------

import time
import sys
import os
#---
import questionary
#---
import controleur_vie

class Ecran():
    """Classe contenant toutes les zones de textes à afficher.
    Permet d'alléger les fonctions de la vue."""

    def ecran_ouverture_jeu(self):
        """Premier affichage à l'ouverture du programme"""
        affiche = """Bienvenu sur mon programme

        Jeu de la vie

        by Silanoc - août 2022"""

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
    """Première fonction appelée au démarage du jeu"""
    efface_console()
    affiche = les_ecrans.ecran_ouverture_jeu()
    print(affiche)
    time.sleep(1)
    menu_principal()

def menu_principal():
    efface_console()
    affiche = les_ecrans.ecran_menu()
    print(affiche)
    #choix = input ("rentrer la lettre demandée.\nNouvelle partie aléatoire (N) \nQuitter(Q)")
    choix_entier = questionary.select("Que voulez-vous faire ?", choices = ['Nouvelle partie aléatoire', 'Quitter']).ask()
    #choix = ""
    if choix_entier == "Nouvelle partie aléatoire":
        choix = 'N'
    elif choix_entier == "Quitter":
        choix = 'Q'
    controleur_vie.gestion_choix_menu_principal(choix)

def nouvelle_partie(grille, grille_de_jeu):
    efface_console()
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    time.sleep(1)
    affiche_une_grille(grille, grille_de_jeu)

def affiche_une_grille(grille, grille_de_jeu):
    """affiche dans la consolle la grille
        pour plus de lisibilité, espace vide si 0 et X si vivant"""

    for ligne in range(grille_de_jeu.nb_ligne):
        affiche = ""
        for colonne in range(grille_de_jeu.nb_colonne):
            if grille_de_jeu.grille[ligne][colonne] == 0:
                affiche += " "
            else:
                affiche += "X"
        print(affiche)
    time.sleep(1)
    #choix = input("encore un tour O/n")
    choix = questionary.confirm("Encore un tour ?", default = True).ask()
    controleur_vie.gestion_demande_nouveau_tour(choix, grille, grille_de_jeu)

def quitter():
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()
