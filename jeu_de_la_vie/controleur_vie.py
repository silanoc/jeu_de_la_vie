#! /usr/bin/env python3
# coding: utf-8

"""Dans une architecture MVC, contrôleur du jeu de la vie."""

import jeu_de_la_vie.vue_vie as vue_vie
import jeu_de_la_vie.modele_vie as modele_vie


def creer_une_grille_initale(nb_ligne: int, nb_colonne: int) -> None:
    """Création d'une grille remplie pour commencer.

    A partir de la classe Automate du module modele_vie, créé une instance grille_de_jeu.
    Chaque cellule a un état 0 ou 1.
    
    Dit au module vue_vie d'exécuter la fonction nouvelle_partie avec l'instance et ces valeurs.

    :param int nb_ligne: nombre de ligne que l'on souhaite pour la grille.
    :param int nb_colonne: nombre de colonne que l'on souhaite pour la grille.
    """
    
    grille_de_jeu = modele_vie.Automate((nb_ligne, nb_colonne))
    grille_de_jeu.grille = grille_de_jeu.remplissage_aleatoire_a_la_creation()
    vue_vie.nouvelle_partie(grille_de_jeu)


def gestion_choix_menu_principal(choix: str) -> None:
    """Appliquer la décision demandée dans vue_vie.menu_principal()

    Selon le choix, demande au module vue_vie d'exécuter une fonction différente.

    :param string choix: valeur déterminée dans vue_vie.menu_principal()
    """
    if choix == "Nouvelle partie aléatoire":
        vue_vie.choix_taille_grille()
        #vue_vie.nouvelle_partie(affichage, grille_de_jeu)
    elif choix == "Quitter":
        vue_vie.quitter()


def gestion_choix_taille(nb_ligne: int, nb_colonne: int) -> None:
    grille_de_jeu = creer_une_grille_initale(nb_ligne, nb_colonne)


def gestion_demande_nouveau_tour(choix: bool, grille_de_jeu) -> None:
    """Appliquer la decision demandée dans vue_vie.affiche_une_grille()

    Selon la décision binaire :

    * Recalcule un génération dans l'instance grille_de_jeu. Et demande à vue_vie de l'afficher.
    * Demande à vue_vie de revenir au menu principal.

    :param bool choix: déterminée dans vue_vie.affiche_une_grille()
    :param  lst grille: liste de liste de 0 ou 1 issus de l'instance grille_de_jeu
    :param grille_de_jeu: l'instance d'Automate
    """
    if choix:
        grille_de_jeu.genere_nouvelle_generation()
        vue_vie.affiche_une_grille(grille_de_jeu)
    else:
        vue_vie.menu_principal()