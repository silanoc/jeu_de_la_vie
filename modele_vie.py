#-------------------------------------------------------------------------------
# Name:        modele vie
# Purpose:
#
# Author:      Gabriel-le
#
# Created:     08/08/2022
# Copyright:   (c) Gabriel-le 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import controleur_vie

class Ecran():
    def ecran_ouverture_jeu(self):
        affiche = """Bienvenu sur mon programme

        Jeu de la vie

        by silanoc - aout 2022"""

        return affiche

    def ecran_menu(self):
        affiche = "Vous avez plusieurs choix"
        return affiche

    def ecran_quitter(self):
        affiche = "Merci d'avoir utilisé ce programme. A une prochaine occasion."
        return affiche

    def ecran_debut_partie(self):
        affiche = "partie en cours"
        return affiche