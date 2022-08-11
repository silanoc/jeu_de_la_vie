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

def test_creation_automate():
    automate = modele_vie.Automate((3,3))
    assert automate.grille == [["", "", ""], ["", "", ""], ["", "", ""]]

pytest.main(args=['-s', os.path.abspath('test_modele_vie.py')])