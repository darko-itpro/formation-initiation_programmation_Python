"""
Ceci est un module destiné à recevoir le code des fonctions mutualisées au sein
des notebooks. Ajoutez donc les fonctions que vous pensez utile.
Notez que dans un projet *normal* un module de ce type ne devrait être dédié
qu'à une seule unité fonctionnelle. Dans le cadre de la formation, nous allns
nous permettre de transgresser ce principe. Mais vous pouvez évidemment créer
d'autres modules (fichiers texte avec l'extension .py).
Notez également que ce commentaire est une documentation du module. Il s'agit
d'une docstring du module.
"""


def duration_for(how_many: int, unit_duration=7):
    """
    Returns the duration for how_namy units of unit_duration.

    :param how_many: the number of units
    :param unit_duration: the duration of an unit
    :return: the product of both parameters.
    """
    return int(how_many) * int(unit_duration)