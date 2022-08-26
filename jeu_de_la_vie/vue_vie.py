#! /usr/bin/env python3
# coding: utf-8

"""dans le modèle MVC le gestionnaire de vue.

Les choix de l'utilisateur sont fait par la bibliothèque questionary"""

import time
import sys
import os

import questionary

import jeu_de_la_vie.controleur_vie as controleur_vie


class Ecran():
    """Classe contenant toutes les zones de textes à afficher.
    Permet d'alléger les fonctions de ce fichier vue_vie.
    """

    def ecran_ouverture_jeu(self):
        """Premier affichage à l'ouverture du programme

        return:
        - affiche (string)
        """
        affiche = """Bienvenu sur mon programme

        Jeu de la vie

        by Silanoc - août 2022"""
        return affiche

    def ecran_menu(self):
        """Message pour le menu principal.
        return:
        - affiche (string)
        """
        affiche = "Vous avez plusieurs choix"
        return affiche

    def ecran_demande_taille_grille(self):
        """Message pour demander la taille voulu pour la grille

        return:
        - affiche (string)
        """
        affiche = """Quelle taille voulez-vous pour la grilel de jeu ?
        Merci de rentrer un nombre entier positif à chaque fois."""
        return affiche

    def ecran_debut_partie(self):
        """Message pour le début de la partie, génération 0

        return:
        - affiche (string)
        """
        affiche = "partie en cours"
        return affiche

    def ecran_quitter(self):
        """Dernier affichage visible par l'utilisateur.

        return:
        - affiche (string)
        """
        affiche = "Merci d'avoir utilisé ce programme. A une prochaine occasion."
        return affiche


# instantiation de l'objet écran.
les_ecrans = Ecran()


def efface_console():
    """Pour nettoyer la console entre chaque vue, et avoir quelque chose de propre"""
    if sys.platform.startswith("win"): #si windows
        os.system("cls")
    else:
        os.system("clear")


def demarer_jeu():
    """Première fonction appelée au démarage du jeu.

    Affiche l'écran d'ouverture puis le menu.
    """
    efface_console()
    affiche = les_ecrans.ecran_ouverture_jeu()
    print(affiche)
    time.sleep(1)
    menu_principal()


def menu_principal():
    """Menu principal.

    Demande un choix à l'utilisateur (commencer une nouvelle partie ou quitter).
    Transmet se choix (string) à la fonction gestion_choix_menu_principal du module controleur_vie.
    """
    efface_console()
    affiche = les_ecrans.ecran_menu()
    print(affiche)
    choix = questionary.select("Que voulez-vous faire ?", choices = ['Nouvelle partie aléatoire', 'Quitter']).ask()
    controleur_vie.gestion_choix_menu_principal(choix)


def choix_taille_grille():
    """L'utilisateur choisi la taille de la grille de jeu

    Demande à l'utilisateur deux nombres entiers positifs ligne et colonne.
    Les transmet à la fonction gestion_choix_taille du module controleur_vie.
    """
    efface_console()
    affiche = les_ecrans.ecran_demande_taille_grille()
    print(affiche)
    ok = False
    while  ok is False or ligne < 0 :
        ligne = questionary.text("nombre de ligne").ask()
        try:
            ligne = int(ligne)
            ok = True
        except:
            ok = False
    ok = False
    while ok is False or colonne < 0:
        colonne = questionary.text("nombre de colonne").ask()
        try:
            colonne = int(colonne)
            ok = True
        except:
            ok = False
    controleur_vie.gestion_choix_taille(ligne, colonne)


def nouvelle_partie(grille, grille_de_jeu):
    """Affiche la génération génération 0

    arg :
    - grille (liste de liste) : 0 ou 1 issus de l'instance grille_de_jeu
    - grille_de_jeu (objet) : l'instance d'Automate
    """
    efface_console()
    affiche = les_ecrans.ecran_debut_partie()
    print(affiche)
    affiche_une_grille(grille, grille_de_jeu)


def affiche_une_grille(grille, grille_de_jeu):
    """Affiche dans la consolle l'état des cellules.
    Pour plus de lisibilité, " " si 0/mort et "X" si 1/vivant

    - grille (liste de liste) : 0 ou 1 issus de l'instance grille_de_jeu
    - grille_de_jeu (objet) : l'instance d'Automate
    """
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
    """Affiche le message final et quitte le programme."""
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()