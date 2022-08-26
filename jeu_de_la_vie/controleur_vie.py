#! /usr/bin/env python3
# coding: utf-8

"""dans une architecture MVC, contrôleur du jeu de la vie."""

import jeu_de_la_vie.vue_vie as vue_vie
import jeu_de_la_vie.modele_vie as modele_vie


def creer_une_grille_initale(ligne, colonne):
    """Création d'une grille rempli pour commencer.

    A partir de la classe Automate du module modele_vie, crré une instance grille de jeu.
    Chaque cellule à un état 0 ou 1.
    Dit au module vue_vie d'exécuter la fonction nouvelle partie avec l'instance et ces valeurs

    arg :
    - ligne (int) : nombre de ligne que l'on souhaite pour la grille
    - colonne (int) : nombre de colonne que l'on souhaite pour la grille
    """
    grille_de_jeu = modele_vie.Automate((ligne, colonne))
    grille_de_jeu.grille = grille_de_jeu.remplissage_aleatoire_a_la_creation()
    vue_vie.nouvelle_partie(grille_de_jeu.grille, grille_de_jeu)


def gestion_choix_menu_principal(choix):
    """Appliquer la decision demandé dans vue_vie.menu_principal()

    Selon le choix, demande au module vue_vie d'exécuter une fonction différente.

    arg:
    - choix (string) : valeur détermnié dans vue_vie.menu_principal()
    """
    if choix == "Nouvelle partie aléatoire":
        vue_vie.choix_taille_grille()
        #vue_vie.nouvelle_partie(affichage, grille_de_jeu)
    elif choix == "Quitter":
        vue_vie.quitter()


def gestion_choix_taille(ligne, colonne):
    grille_de_jeu = creer_une_grille_initale(ligne, colonne)


def gestion_demande_nouveau_tour(choix, grille, grille_de_jeu):
    """Appliquer la decision demandé dans vue_vie.affiche_une_grille()

    Selon la décision binaire
    - recalcule un génération dans l'instance grille_de_jeu. 
    Et demande à vue_vie de l'afficher.
    - Demande à vue_vie de revenir au menu principal.

    arg:
    - choix (boolean) : déterminé dans vue_vie.affiche_une_grille()
    - grille (liste de liste) : 0 ou 1 issus de l'instance grille_de_jeu
    - grille_de_jeu (objet) : l'instance d'Automate
    """
    if choix:
        grille_de_jeu.genere_nouvelle_generation()
        grille = grille_de_jeu.grille
        vue_vie.affiche_une_grille(grille, grille_de_jeu)
    else:
        vue_vie.menu_principal()