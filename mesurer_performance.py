#! /usr/bin/env python3
# coding: utf-8

import vie
import time

vie_script = vie.Automate((150, 150))
nb_generation: int = 10

print("---generation initiale-------")
vie_script.grille = vie_script.remplissage_aleatoire_a_la_creation()
#vie_script.affichage_grille()

for i in range(1, nb_generation + 1):    
    print(f"---generation {i}-------")
    ti: float = time.time()
    vie_script.genere_nouvelle_generation()
    tf: float = time.time()
    print(f"temps calcul d'une génération : {tf - ti}")
    #vie_script.affichage_grille()
