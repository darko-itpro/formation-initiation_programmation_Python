# 01 ‐ Valeurs et variables

Pour découvrir la programmation avec le langage Python, nous allons construire un programme pas à pas.

Nous allons travailler dans le package `exos` qui regroupera tout votre code de la formation.

## Rappels
Un *package* est un répertoire contenant un fichier `__init__.py` . Un package contient d’autres 
packages et/ou des modules.

Un *module* est un fichier texte contenant du code python et portant l’extension .py.

## Premier exercice
Créez un fichier source dans le répertoire `exos` que vous appellerez `exo_01a.py` .

Votre formation a une **durée de 3 jours**, chaque jour ayant une **durée de 7 heures**.

Dans votre script :

* affectez ces valeurs à des variables.
* Affichez les valeurs de ces variables.
* Calculez la durée totale en heure de votre formation et affichez cette durée.

Nous allons d’ailleurs voir comment un code bien organisé aide à être maintenu : je me suis trompé, 
la formation a une durée de 2 jours.

Corrigez le code pour utiliser cette valeur. Logiquement, vous n’avez qu’un caractère à corriger 
avant de ré-exécuter le module.

## Second exercice
Créez un nouveau fichier source que vous nommerez `exo_01b.py` pour ce second exercice.

La pause de midi du premier jour a durée 72 minutes. Affichez combien cela fait en heure(s) et 
minutes (vous pouvez évidemment afficher d’une part les heures et d’autre part les minutes).

## Troisième exercice
Dans le répertoire `exos`, vous trouverez un fichier `exo_01c.py`. Ce fichier contient du code qui 
interagit avec l’utilisateur. Il demande dans le terminal la durée de la formation en jours. Cette 
valeur est affectée à la variable `duration`.

Utilisez le code existant pour afficher la valeur de cette durée **en heures**. Faites bien 
attention à la donnée retournée par la fonction…