# 06 ‐ Les dictionnaires

Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :
* `exos/exo_06.py`qui vous est fourni.

Nous allons travailler sur une notion de formations plus *complexe*.

Nous avons déjà vu un exemple de donnée structurée sous forme de liste dans les exercices précédents.

Il s’agit d’un type de représentation de données que vous obtiendrez dans certains cas comme lors 
de la lecture de fichiers CSV ou l’interrogation de bases de données. Mais cette structure est 
« peu pratique ». Aussi, nous allons travailler sur des données structurées en dictionnaires.

Le fichier `exos/exo_06.py` vous propose quelques données dont, par exemple, 

```python
training_to_maintain = {"title": "Python, initiation",
                        "duration": 2,
                        "price": 1200,
                        "students": 5,
                        }
```

## Rappels
### Accéder à une valeur
`my_dict[key]` retourne la valeur associée à `key`

### Vérifier si une clef existe dans le dictionnaire
`key in my_dict` retourne `True` si `key` est une clef du dictionnaire, sinon `False`.

### Modifier la valeur associée à une clef ou créer le couple clef/valeur
`my_dict[key] = value`, si `key` est une clef du dictionnaire, sa valeur est modifiée sinon le 
couple est créé.

## Prise en main des dictionnaires
Commencez par prendre en main le dictionnaire en accédant aux différents champs ou en modifiant la 
valeur associée.

## Une fonction pour savoir si l’épisode est vu
Nous allons devoir adapter notre fonction. Créez une nouvelle fonction 
`is_maintained(training:dict)` dans ce fichier. Cette fonction doit retourner `True` si la 
formation est assurée sinon `False`. Testez avec les différentes variables.