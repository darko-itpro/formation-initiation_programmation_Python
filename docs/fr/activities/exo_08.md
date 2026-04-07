# 08 ‐ Les listes, deuxième partie

Nous allons lancer un service de formation. Nous avons une liste d'inscrits pour une formation 
Python **limitée à 12 places**.

Voici la liste des inscrits :
```python
students = [{'name': 'Éric de Voisin', 'company': 'Petitjean Bonnet et Fils'},
            {'name': 'Richard Lamy', 'company': 'Bertin SA'},
            {'name': 'Auguste Jourdan-Hernandez', 'company': 'Nguyen'},
            {'name': 'Antoine Gaudin', 'company': 'Fournier'},
            {'name': 'Capucine Bonnin du Bourgeois', 'company': 'Pelletier'},
            {'name': 'Denise Rocher', 'company': 'Gosselin Boyer et Fils'},
            {'name': 'Édouard Le Goff', 'company': 'Lemaire'},
            {'name': 'Simone Chartier de la Richard', 'company': 'Bazin'},
            {'name': 'Dominique Langlois', 'company': 'Chevallier'},
            {'name': 'Denis-Roger Blot', 'company': 'Albert et Fils'},
            {'name': 'Jacques Rousset', 'company': 'Devaux SARL'},
            {'name': 'Georges Ledoux', 'company': 'Benard'},
            {'name': 'Louise Maillet Le Maury', 'company': 'Auger Ruiz S.A.R.L.'},
            {'name': 'Audrey Martin', 'company': 'Rocher Daniel S.A.'},
            {'name': 'Frédéric Diaz-Pons', 'company': 'Lacombe'},
            {'name': 'Patricia-Alexandria Maréchal', 'company': 'Leleu'},
            {'name': 'Émile Cohen', 'company': 'Poirier et Fils'},
            {'name': 'Maurice Evrard', 'company': 'Guilbert'},
            {'name': 'Adélaïde Morel du Germain', 'company': 'Bigot'},
            {'name': 'Marc Roche', 'company': 'Pages S.A.'}]
```

Recopiez cette liste dans vos sources.

## Première question
À partir de cette liste, créez une liste des personnes qui suivront la formation. Il s'agit des N 
premiers de cette liste `students` où N est le nombre de places disponibles pour la formation.

Créez une deuxième liste qui représente la liste d'attente, c'est à dire à partir d'après le 
dernier stagiaire affecté à la formation jusqu'à la fin.

Créez la fonction `get_training_groups(registered_students: list, max_students: int) -> tuple(list, list)`
et déplacez-y le code.

Cette fonction doit donc retourner deux listes : la liste des inscrits à la formation et la liste 
d'attente. 

## Deuxième question
Si votre code fonctionne, utilisez comme paramètre d'entrée la liste suivante (la liste est réduite 
à 10 stagiaires) :
```python
students = [{'name': 'Éric de Voisin', 'company': 'Petitjean Bonnet et Fils'},
            {'name': 'Richard Lamy', 'company': 'Bertin SA'},
            {'name': 'Auguste Jourdan-Hernandez', 'company': 'Nguyen'},
            {'name': 'Antoine Gaudin', 'company': 'Fournier'},
            {'name': 'Capucine Bonnin du Bourgeois', 'company': 'Pelletier'},
            {'name': 'Denise Rocher', 'company': 'Gosselin Boyer et Fils'},
            {'name': 'Édouard Le Goff', 'company': 'Lemaire'},
            {'name': 'Simone Chartier de la Richard', 'company': 'Bazin'},
            {'name': 'Dominique Langlois', 'company': 'Chevallier'},]
```

Est-ce que votre code fonctionne toujours ?
