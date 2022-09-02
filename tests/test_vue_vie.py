#! /usr/bin/env python3
# coding: utf-8

"""Série de tests pour le fichier jeu_de_la_vie.vue_vie"""

import pytest
import os

import questionary

import jeu_de_la_vie.vue_vie as vue_vie

# Ligne nécessaire pour certaines configurations
pytest.main(args=['-s', os.path.abspath('test_vue_vie.py')])

class Testvue_vie():
    """Objet contenant tous les tests."""
    
    def test_existance_Ecran(self) -> None:
        """Vérifie l'existance de la classe Ecran, et son __init__. 
        Vérifie que chacune des méthode génére un str autre qu'une chaine vide."""
        ecran = vue_vie.Ecran()
        assert type(ecran.ecran_ouverture_jeu()) == str and ecran.ecran_ouverture_jeu() != ""
        assert type(ecran.ecran_menu()) == str and ecran.ecran_menu() != ""
        assert type(ecran.ecran_demande_taille_grille()) == str and ecran.ecran_demande_taille_grille() != ""
        assert type(ecran.ecran_debut_partie()) == str and ecran.ecran_debut_partie() != ""
        assert type(ecran.ecran_quitter()) == str and ecran.ecran_quitter() != ""
        
    def test_demande_int_superieur_zero(self):
        """il faut penser à faire pytest -s pour demander la main"""
        nb = vue_vie.demande_int_superieur_zero("ma question de test, entrer un int > 0")
        assert type(nb) == int and nb > 0