# 05 ‐ Les conditionnelles, seconde partie

Les deux exercices sont indépendants.

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :
* `exos/training_utils.py`que vous avez créé précédemment (il peut avoir un nom différent improvisé 
* lors de la formation).

## Exercice
Après la mise en production, nous avons découvert qu'il pouvait y avoir deux structures de données 
pour un formation **qui devra être annulée** :

```python
training_to_cancel = ["Python, initiation", 2, 1200, 0]
training_to_cancel = ["Django, initiation", 4, 2200]
```

La première contient un entier représentant le nombre de participants en quatrième position et le 
second n’a que 3 valeurs.

Si vous utilisez cette seconde donnée avec votre fonction, elle lèvera une exception.

Faite évoluer la fonction pour qu’une formation n’ayant pas l’information « nombre d'inscrits » 
(qui n’a donc que 3 données) soit considéré comme « à annuler ».