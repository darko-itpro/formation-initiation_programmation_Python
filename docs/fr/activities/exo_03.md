# 03 ‐ Les conditionnelles

## Aide mémoire
La structure d’une condionnelle est

```python
if condition:
    code
```

Celle du si…sinon
```python
if condition:
    code
else:
    code
```

Enfin, le si…sinon si…()…sinon
```python
if condition:
    code
elif condition:
    code
else:
    code
```


## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :
* `exos/exo_03_01.py`qui vous est fourni.
* `exos/exo_03_02.py`qui vous est fourni.

## Premier exercice
Le fichier source `exo_03_01.py` contient la déclaration de deux variables auxquelles sont 
affectées des données correspondant à deux formations : un formation qui sera assurée et une qui 
devra être annulée.

Ce code déclare également une variable `training` à laquelle est affectée une des variables 
précédente et une ligne en commentaire où c’est l’autre. Vous allez travailler sur la variable 
`training`, ainsi, pour *tester* l’un ou l’autre comportement, il vous suffira de commenter l’une 
ou l’autre ligne.

* Ecrivez le code qui affichera « la formation est assurée » si la formation… est maintenue et rien 
* si elle sera annulée.
* Complétez le code pour qu’il affiche « la formation est maintenue » si la formation est maintenue 
* et « la formation est annulée » si elle sera annulée.

Le code que vous écrirez pourra être « parlant ».

## Second exercice
Le ficher source `exo_03_02.py` contient un code similaire mais l’information maintenue ou non est 
représentée par un entier représentant le nombre d'inscrits. Nous partons du principe que si il y a 
au moins un inscrit, la formation sera assurée.

Reprenez les questions précédentes pour cette représentation de données.