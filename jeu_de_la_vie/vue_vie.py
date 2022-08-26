#-------------------------------------------------------------------------------
# Name:        vue vie
# Purpose:     dans le modèle MVC le gestionnaire de vue.
#
# Author:      silanoc
#
# Created:     08/08/2022
# Version :    1.1
#-------------------------------------------------------------------------------

import time
import sys
import os
#---
import questionary
#---
import jeu_de_la_vie.controleur_vie as controleur_vie

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

    def ecran_demande_taille_grille(self):
        affiche = """Quelle taille voulez-vous pour la grilel de jeu ?
        Merci de rentrer un nombre entier positif à chaque fois."""
        return affiche

    def ecran_debut_partie(self):
        affiche = "partie en cours"
        return affiche

    def ecran_quitter(self):
        affiche = "Merci d'avoir utilisé ce programme. A une prochaine occasion."
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
    choix = questionary.select("Que voulez-vous faire ?", choices = ['Nouvelle partie aléatoire', 'Quitter']).ask()
    controleur_vie.gestion_choix_menu_principal(choix)

def choix_taille_grille():
    efface_console()
    affiche = les_ecrans.ecran_demande_taille_grille()
    print(affiche)
    ok = False
    while  ok == False or ligne < 0 :
        ligne = questionary.text("nombre de ligne").ask()
        try:
            ligne = int(ligne)
            ok = True
        except:
            ok = False
    ok = False
    while ok == False or colonne < 0:
        colonne = questionary.text("nombre de colonne").ask()
        try:
            colonne = int(colonne)
            ok = True
        except:
            ok = False
    controleur_vie.gestion_choix_taille(ligne, colonne)

def nouvelle_partie(grille, grille_de_jeu):
    efface_console()
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    affiche_une_grille(grille, grille_de_jeu)

def affiche_une_grille(grille, grille_de_jeu):
    """affiche dans la consolle la grille
        pour plus de lisibilité, espace vide si 0 et X si vivant"""
    efface_console()
    for ligne in range(grille_de_jeu.nb_ligne):
        affiche = ""
        for colonne in range(grille_de_jeu.nb_colonne):
            if grille_de_jeu.grille[ligne][colonne] == 0:
                affiche += " "
            else:
                affiche += "X"
        print(affiche)
    print("\n") #pour espacer la grille et l'invite de commande
    choix = questionary.confirm("Encore un tour ?", default = True).ask()
    controleur_vie.gestion_demande_nouveau_tour(choix, grille, grille_de_jeu)

def quitter():
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()
