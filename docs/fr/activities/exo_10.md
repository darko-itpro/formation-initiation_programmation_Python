# 10 ‐ Les boucles

Dans un nouveau fichier, déclarez la formation :
```python
first_training = {"title":"Python, les fondamentaux",
                  "duration": 5,
                  "max_students": 8,
                  "students": [],
                 }
```

Déclarez également la liste des stagiaires des exercices précédents

## Premier exercice
Écrivez une boucle qui itérer sur la liste des stagiaires et les affecter à la formation grâce à la 
fonction précédente. Dans cette première version, il y aura plus d'inscrits que de places.

## Seconde exercice
Modifiez la boucle pour arrêter d'ajouter des participants une fois que la formation est pleine.

## Troisième exercice
Modifiez votre code pour pouvoir créer, une fois la formation remplie, une liste d'attente 
`wait_list` contenant les stagiaires qui n'ont pas été affectés à la formation. Si tous les 
stagiaires ont été affecté à la formation, la liste `wait_list` doit être vide.