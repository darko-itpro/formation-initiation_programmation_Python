# Initiation Programmation

This is the practical cases for the computer programming training I provide.
Intended for french trainee, the rest of the explanations are in french.

Ce référentiel est le support de ma formation d'initiation à la programmation.
Il est destiné à mes stagiaires.

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/initiation-programmation/blob/master/LICENSE)

Ces sources sont organisées pour suivre le déroulement de la formation tout en
respectant l'organisation d'un package.

## Mise en place de l'environnement
### Procédure standard
Le gestionnaire de dépendances [pip](https://pypi.python.org/pypi/pip) doit être
installé et accessible.

Deux dépendances sont nécessaires : Jupyter et iPython. iPython étant une
dépendance de Jupyter, vous ne devez installer que ce dernier par l'instruction

Pour mettre à jour l'environnement, Assurez-vous dans un premier temps que
est installé. Placez vous alors à la
racine du projet. Puisque le projet ne nécessite qu'une seule dépendance, vous
pouvez exécuter l'instruction

```
pip install jupyter
```
Un projet Python comporte un fichier requirements.txt qui est un *pip
requirement file*. Il décrit les dépendances nécessaires et permet de les
installer d'un coup toutes les dépendances nécessaires par l'instruction
suivante :

```
pip install -r requirements.txt
```

### Avec Anaconda
Anaconda est une plate-forme destinée au Data Science qui intègre tous les
outils dédiés. Jupyter est donc une dépendance incluse dans Anaconda. L'outil
est beaucoup plus volumineux mais a l'avantage de permettre de contourner
tout problème lié à l'accès à Internet dans le cadre de la formation.

Pous pouvez télécharger Anaconda sur le [site officiel](https://www.anaconda.com/).

## Cahiers d'exercices
Le répertoire *workbooks* contient des *cahiers d'exercices*. Ceux-ci sont
des documents type *Jupyter Notebooks* générés à l'aide de
[Jupyter](http://jupyter.org/).
 
Placez-vous à la racine du projet et exécutez la commande

```
jupyter notebook
```

Vous pouvez maintenant travailler avec les *notebooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://drive.google.com/drive/folders/0B0VMWUAuE_ZFU0ZrY2hDUC1XTlU?resourcekey=0-vOw0a3-hysmCsuKOwi3qkA&usp=sharing).
