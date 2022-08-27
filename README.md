# Jeu de la vie
- Author:      silanoc
- Created:     08/08/2022
- Last edit:   27/08/2022
- Version :    1.2

Pour lancer le jeu
```python3 main.py```

Documentation
```build/html/index.html```

# Description

Programme exécutant le "jeu de la vie", célèbre automate cellulaire.

Il est développé avec l'architecture : Modèle - Vue - Contrôleur.

L'interface est la console.
Les choix sont faits via la librairie questionary.

Framework pour les tests : pytest

La documentation est générée par sphinx
- tutoriel utilisé : https://blog.flozz.fr/2020/09/07/introduction-a-sphinx-un-outil-de-documentation-puissant/

# Les branches
## En cours
- master : la branche valide.
- mesurer_performance : branche pour tester différents algorithmes du moteur du jeu de la vie.
## Stables
- version_1_1 : version avec interface questionary et tests.
- version_1_0 : première version aboutie. Interface par simple input.
- demonstrateur : archive. Juste le fichier avec la classe automate. Première version.
## Travail
- code_review : pour modifier suite à ma demande de relecture sur un groupe facebook
- questionary : branche de développement, pour passer de input à la bibliothèque questionary.
- MVC : délété. Pour passer du démonstrateur à une architecture MVC.

# Les fichiers :
+-- main.py : le runner
|
+-- jeu_de_la_vie : le mécanisme du jeu
|   |
|   +-- modele_vie.py : le modèle
|   +-- vue_vie.py : la vue_vie
|   +-- controleur_vie.py : le contrôleur.
|
+-- tests
|   |
|   +-- test_modele_vie.py : fichier de test pour "modele_vie.py"
|
+-- build/html : la documentation
