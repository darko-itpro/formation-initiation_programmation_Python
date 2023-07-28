# Initiation Programmation

This is the practical cases for the computer programming training I provide.
Intended for french trainee, the rest of the explanations are in french.

Ce référentiel est le support de ma formation d'initiation à la programmation.
Il est destiné à mes stagiaires.

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/initiation-programmation/blob/master/LICENSE)

Ces sources sont organisées pour suivre le déroulement de la formation tout en
respectant l'organisation d'un package.

## Mise en place de l'environnement
### Installer Python
Python doit être installé sur votre système. Vous pouvez récupérer un installeur pour votre
système sur le site de la fondation : https://www.python.org.

La version minimum conseillée est la 3.9. La formation peut être suivie jusqu'à la 3.6 (obsolète)

### Installation de dépendances
Cette formation ne nécessite pas de dépendances et peut-être suivie avec uniquement le contenu
de la distribution standard.

Quelques outils peuvent néanmoins être utiles ou abordés.

La gestion des dépendances est réalisée avec [pip](https://pypi.python.org/pypi/pip) qui est
fourni avec la distribution standard.

**Attention** : `pip` utilise des ports dédiés pour communiquer avec les dépôts. Si vous êtes
derrière un Firewall, il sera nécessaire de lui communiquer le proxy.

Vous pouvez installer une dépendance spécifique avec une instruction sur le modèle :

```shell
pip install ipython
```

Cette instruction à exécuter dans un terminal (bash, zsh, ms-dos ou PowerShell) permet
d'installer la dépendance `ipython`.

Un projet Python comporte un fichier `requirements.txt` qui est un *pip
requirement file*. Il décrit les dépendances nécessaires et permet de les
installer d'un coup toutes les dépendances nécessaires par l'instruction
suivante :

```shell
pip install -r requirements.txt
```

L'environnement est alors prêt à l'emploi.

## Dépendances du projet
Le fichier requirements liste les dépendances nécessaires au projet dans son
ensemble. Il s'agit de :
 * [ipython](https://ipython.org) : shell intéractif plus riche que le shell intéractif standard
 * [Pytest](https://docs.pytest.org/) : utilisé si la notion de tests unitaires est abordée

## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://drive.google.com/drive/folders/0B0VMWUAuE_ZFU0ZrY2hDUC1XTlU?resourcekey=0-vOw0a3-hysmCsuKOwi3qkA&usp=sharing).
