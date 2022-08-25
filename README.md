# Jeu de la vie
- Author:      silanoc
- Created:     08/08/2022
- Version :    1.1

# Description

Programme exécutant le "jeu de la vie", célèbre automate cellulaire.

Il est développé avec l'architecture : Modèle - Vue - Contrôleur.

L'interface est la console.
Les choix sont faits via la librairie questionary.

Framework pour les tests : pytest

# Les branches
## En cours
- master : la branche valide.
- mesurer_preformance : branche pour tester différents algorithmes du moteur du jeu de la vie.
## Stables
- version_1_0 : première version aboutie. Interface par simple input.
- version_1_1 : version avec interface questionary et tests.
- demonstrateur : archive. Juste le fichier avec la classe automate. Première version.
## Travail
- questionary : branche de développement, pour passer de input à la bibliothèque questionary.
- MVC : délété. Pour passer du démonstrateur à une architecture MVC.

# Les fichiers :
- jeu_vie.py : pour démarrer le programme. Seul fichier possédant une structure
```if __name__ == __main__```
- modele_vie.py : le modèle
- vue_vie.py : la vue_vie
- controleur_vie.py : le contrôleur.
- test_modele_vie.py : fichier de test pour "modele_vie.py"

