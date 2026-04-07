# 07 ‐ Les fonctions, seconde partie

## Fichiers de travail
Le code de base est celui du fichier contenant votre fonction `is_maintained(training:dict)`. Les 
diverses parties de cet exercice vous demanderont de faire des versions différentes de la fonction 
aussi pour en garder une trace, recopiez le code dans de nouveaux fichiers.

## Première version
Nous allons modifier la fonction pour prendre en compte un nombre minimum de participants pour 
assurer une formation. En effet, certaines nécessitent plus d'un inscrit. La fonction doit donc 
devenir `is_maintained(training:dict, min_students:int)`. Ce second paramètre représente le nombre 
minimum d'inscrits pour assurer la formation.

Modifiez la fonction pour qu'elle prenne en compte ce paramètre et essayez avec plusieurs valeurs.

## Première version, évolution
Le problème d'ajouter un paramètre est que les appels de l'exercice précédents ne fonctionnent pas. 
Le code que vous avez écrit précédemment ne fonctionne donc plus. Modifiez la fonction pour que ce 
deuxième paramètre soit optionnel.

## Seconde version
Finalement, après quelques tests, cette version n'est pas satisfaisante. Le nombre de participants 
n'est pas une valeur fiable. Nous savons quel est le cout d'une formation (location de salle, 
salaires…). Modifiez la fonction pour quelle devienne `is_maintained(training:dict, cost:float)`. 
La formation sera assurée si le bénéfice est supérieur ou égal à 110% du cout de la formation.

Mais ce paramètre doit être optionnel. Si il est absent, la formation sera assurée si il y a au 
moins un participant.
