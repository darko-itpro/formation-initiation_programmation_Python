# 09 ‐ Les listes, troisième partie

Soit une formation représentée sous forme du dictionnaire suivant :

```python
training = {"title":"Python, les fondamentaux",
            "duration": 5,
            "max_students": 8,
            "students": [],
           }
```

## Première question
Écrivez une fonction `add_student(training:dict, student:dict)` qui ajoute un stagiaire à une 
formation. Pour tester, vous pouvez utiliser la donnée de formation ci-dessus et une donnée de 
stagiaire de l'exercice précédent.

## Seconde question
Dans un nouveau fichier, recopiez le code suivant :
```python
first_training = {"title":"Python, les fondamentaux",
                  "duration": 5,
                  "max_students": 8,
                  "students": [],
                 }
```

Copiez ensuite cette formation dans une nouvelle variable `second_training`. Nous avons donc deux 
formations.

Ajoutez un participant à chaque formation. 

Vérifiez que tout s'est bien passé.