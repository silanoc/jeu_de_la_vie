#! /usr/bin/env python3
# coding: utf-8

"""Série de tests pour le fichier jeu_de_la_vie.modele_vie"""

import pytest
import os
import jeu_de_la_vie.modele_vie as modele_vie

# Ligne nécessaire pour certaines configurations
pytest.main(args=['-s', os.path.abspath('test_modele_vie.py')])

class Testmodele_vie():
    """Objet contenant tous les tests."""

    def test_creation_automate(self) -> None:
        """Vérifie l'existance de la classe automate, et son __init__. 
        Vérifie qu'il génére bien une liste de liste contenant 99."""
        automate = modele_vie.Automate((3,3))
        assert automate.grille == [[99, 99, 99], [99, 99, 99], [99, 99, 99]]

    def test_remplissage_aleatoire_a_la_creation(self) -> None:
        """Test la méthode automate.remplissage_aleatoire_a_la_creation()."""
        automate = modele_vie.Automate((3,3))
        remplissage: list[list[int]] = automate.remplissage_aleatoire_a_la_creation()
        #remplissage = automate.grille
        assert len(remplissage) == 3 and len(remplissage[0]) == 3

    def test_calcul_etat_initial(self) -> None:
        """Test la methode automate.calcul_etat_initial().
        Une grille de 0 et 1 est donné, une grille de valeurs entre 0 à 8 doit être générée."""
        automate = modele_vie.Automate((6,6))
        automate.grille = [[1,1,0,0,0,0],
                            [1,1,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,1,1,1],
                            [0,0,0,0,0,0],
                            [1,0,0,0,0,0]]
        grille_de_calcul: list[list[int]] = automate.calcul_etat_initial()
        assert grille_de_calcul == [[3,3,2,0,0,0],
                                    [3,3,2,0,0,0],
                                    [2,2,2,2,3,2],
                                    [0,0,1,1,2,1],
                                    [1,1,1,2,3,2],
                                    [0,1,0,0,0,0]]

    def test_donne_etat_final(self) -> None:
        """Test la méthode  automate.donne_etat_final.
        Une grille de valeur initale et de nombre de voisne est donnée.
        Doit générer une grilel de 0 et 1."""
        automate = modele_vie.Automate((6,6))
        automate.grille = [[1,1,0,0,0,0],
                            [1,1,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,1,1,1],
                            [0,0,0,0,0,0],
                            [1,0,0,0,0,0]]
        grille_de_calcul: list[list[int]] = [[3,3,2,0,0,0],
                            [3,3,2,0,0,0],
                            [2,2,2,2,3,2],
                            [0,0,1,1,2,1],
                            [1,1,1,2,3,2],
                            [0,1,0,0,0,0]]
        automate.donne_etat_final(grille_de_calcul)
        assert automate.grille == [[1,1,0,0,0,0],
                            [1,1,0,0,0,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,0,0]]

    def test_genere_nouvelle_generation(self) -> None:
        """Test la méthode automate.genere_nouvelle_generation().
        Une grille de 0 et 1 est donnée, une nouvelel grille doit être calculée."""
        automate = modele_vie.Automate((6,6))
        automate.grille = [[1,1,0,0,0,0],
                            [1,1,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,1,1,1],
                            [0,0,0,0,0,0],
                            [1,0,0,0,0,0]]
        automate.genere_nouvelle_generation()
        assert automate.grille == [[1,1,0,0,0,0],
                            [1,1,0,0,0,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,0,0]]