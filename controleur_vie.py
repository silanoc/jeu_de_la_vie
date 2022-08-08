#-------------------------------------------------------------------------------
# Name:        controleur vie
# Purpose:
#
# Author:      Gabriel-le
#
# Created:     08/08/2022
# Copyright:   (c) Gabriel-le 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import vue_vie
import modele_vie


def gestion_choix_menu_principal(choix):
    if choix == "N":
        vue_vie.nouvelle_partie()
    elif choix == "Q":
        vue_vie.quitter()








