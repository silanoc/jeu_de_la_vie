#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gabriel-le
#
# Created:     11/08/2022
# Copyright:   (c) Gabriel-le 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pytest
import os
import modele_vie

pytest.main(args=['-s', os.path.abspath('test_modele_vie.py')])

def test_creation_automate():
    automate = modele_vie.Automate((3,3))
    assert automate.grille == [["", "", ""], ["", "", ""], ["", "", ""]]

def test_remplissage_aleatoire_a_la_creation():
    automate = modele_vie.Automate((3,3))
    remplissage = automate.remplissage_aleatoire_a_la_creation()
    #remplissage = automate.grille
    assert len(remplissage) == 3 and len(remplissage[0]) == 3

def test_calcul_etat_initial():
    automate = modele_vie.Automate((6,6))
    automate.grille = [[1,1,0,0,0,0],
                        [1,1,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,1,1,1],
                        [0,0,0,0,0,0],
                        [1,0,0,0,0,0]]
    grille_de_calcul = automate.calcul_etat_initial()
    assert grille_de_calcul == [[3,3,2,0,0,0],
                                [3,3,2,0,0,0],
                                [2,2,2,2,3,2],
                                [0,0,1,1,2,1],
                                [1,1,1,2,3,2],
                                [0,1,0,0,0,0]]

def test_donne_etat_final():
    automate = modele_vie.Automate((6,6))
    automate.grille = [[1,1,0,0,0,0],
                        [1,1,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,1,1,1],
                        [0,0,0,0,0,0],
                        [1,0,0,0,0,0]]
    grille_de_calcul = [[3,3,2,0,0,0],
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


