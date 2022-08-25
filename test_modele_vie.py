#-------------------------------------------------------------------------------
# Name:        test_modele_vie
# Purpose:     série de tests pour le fichier modele_vie
#
# Author:      Silanoc
#
# Created:     11/08/2022
# Version :    1.1
#-------------------------------------------------------------------------------

import pytest
import os
import modele_vie

pytest.main(args=['-s', os.path.abspath('test_modele_vie.py')])

class Testmodele_vie():

    def test_creation_automate(self):
        automate = modele_vie.Automate((3,3))
        assert automate.grille == [["", "", ""], ["", "", ""], ["", "", ""]]

    def test_remplissage_aleatoire_a_la_creation(self):
        automate = modele_vie.Automate((3,3))
        remplissage = automate.remplissage_aleatoire_a_la_creation()
        #remplissage = automate.grille
        assert len(remplissage) == 3 and len(remplissage[0]) == 3

    def test_calcul_etat_initial(self):
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

    def test_donne_etat_final(self):
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

    def test_genere_nouvelle_generation(self):
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