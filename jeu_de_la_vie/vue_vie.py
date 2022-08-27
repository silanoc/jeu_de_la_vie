#! /usr/bin/env python3
# coding: utf-8

"""Dans le modèle MVC le gestionnaire de vue.

Les choix de l'utilisateur sont fait par la bibliothèque questionary."""

import time
import sys
import os

Grille_type= list[list[int]] 


import questionary

import jeu_de_la_vie.controleur_vie as controleur_vie


class Ecran():
    """Classe contenant toutes les zones de textes à afficher.
    Permet d'alléger les fonctions de ce fichier vue_vie.
    """

    def ecran_ouverture_jeu(self) -> str:
        """Premier affichage à l'ouverture du programme.

        :returns: affiche 
        :rtype: string
        """
        affiche: str = """Bienvenu sur mon programme

        Jeu de la vie

        by Silanoc - août 2022"""
        return affiche

    def ecran_menu(self)-> str:
        """Message pour le menu principal.

        :returns: affiche 
        :rtype: string
        """
        affiche: str = "Vous avez plusieurs choix"
        return affiche

    def ecran_demande_taille_grille(self) -> str:
        """Message pour demander la taille voulue pour la grille.

        :returns: affiche 
        :rtype: string
        """
        affiche: str = """Quelle taille voulez-vous pour la grille de jeu ?
        Merci de rentrer un nombre entier positif à chaque fois."""
        return affiche

    def ecran_debut_partie(self) -> str:
        """Message pour le début de la partie, génération 0.

        :returns: affiche 
        :rtype: string
        """
        affiche: str = "partie en cours"
        return affiche

    def ecran_quitter(self) -> str:
        """Dernier affichage visible par l'utilisateur.

        :returns: affiche 
        :rtype: string
        """
        affiche: str = "Merci d'avoir utilisé ce programme. A une prochaine occasion."
        return affiche


# instantiation de l'objet écran.
les_ecrans: Ecran = Ecran()


def efface_console() -> None:
    """Pour nettoyer la console entre chaque vue, et avoir quelque chose de propre."""
    if sys.platform.startswith("win"): #si windows
        os.system("cls")
    else:
        os.system("clear")


def demarer_jeu() -> None:
    """Première fonction appelée au démarage du jeu.

    Affiche l'écran d'ouverture puis le menu principal.
    """
    efface_console()
    affiche: str = les_ecrans.ecran_ouverture_jeu()
    print(affiche)
    time.sleep(1)
    menu_principal()


def menu_principal() -> None:
    """Menu principal.

    Demande un choix à l'utilisateur (commencer une nouvelle partie ou quitter).
    Transmet ce choix (string) à la fonction gestion_choix_menu_principal du module controleur_vie.
    """
    efface_console()
    affiche: str = les_ecrans.ecran_menu()
    print(affiche)
    choix: str = questionary.select("Que voulez-vous faire ?", choices = ['Nouvelle partie aléatoire', 'Quitter']).ask()
    controleur_vie.gestion_choix_menu_principal(choix)


def choix_taille_grille() -> None:
    """L'utilisateur choisi la taille de la grille de jeu.

    Demande à l'utilisateur deux nombres entiers positifs ligne et colonne.
    Les transmet à la fonction gestion_choix_taille du module controleur_vie.
    """
    efface_console()
    affiche: str = les_ecrans.ecran_demande_taille_grille()
    print(affiche)
    ok: bool = False
    while  ok is False or ligne < 0 :
        ligne: int = questionary.text("nombre de ligne").ask()
        try:
            ligne: int = int(ligne)
            ok: bool = True
        except:
            ok: bool = False
    ok: bool = False
    while ok is False or colonne < 0:
        colonne:int = questionary.text("nombre de colonne").ask()
        try:
            colonne: int = int(colonne)
            ok: bool = True
        except:
            ok: bool = False
    controleur_vie.gestion_choix_taille(ligne, colonne)


def nouvelle_partie(grille_de_jeu) -> None:
    """Affiche la génération génération 0

    :param list grille: (liste de liste), 0 ou 1 issus de l'instance grille_de_jeu.
    :param grille_de_jeu: l'instance d'Automate.
    """
    efface_console()
    affiche: str = les_ecrans.ecran_debut_partie()
    print(affiche)
    affiche_une_grille(grille_de_jeu)


def affiche_une_grille(grille_de_jeu) -> None:
    """Affiche dans la consolle l'état des cellules.
    Pour plus de lisibilité, " " si 0/mort et "X" si 1/vivant.

    :param list grille: (liste de liste), 0 ou 1 issus de l'instance grille_de_jeu.
    :param grille_de_jeu: l'instance d'Automate.
    """
    efface_console()
    for ligne in range(grille_de_jeu.nb_ligne):
        affiche:str = ""
        for colonne in range(grille_de_jeu.nb_colonne):
            if grille_de_jeu.grille[ligne][colonne] == 0:
                affiche += " "
            else:
                affiche += "X"
        print(affiche)
    print("\n") #pour espacer la grille et l'invite de commande
    choix: bool = questionary.confirm("Encore un tour ?", default = True).ask()
    controleur_vie.gestion_demande_nouveau_tour(choix, grille_de_jeu)


def quitter() -> None:
    """Affiche le message final et quitte le programme."""
    efface_console()
    affiche = les_ecrans.ecran_quitter()
    print(affiche)
    exit()