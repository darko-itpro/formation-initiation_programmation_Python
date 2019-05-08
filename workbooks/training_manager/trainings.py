#!/usr/bin/env python

"""Module de gestion de formations"""


def create_training(name: str, duration: int = 1):
    """
    Crée une nouvelle formation.

    :param name: titre de la formation
    :param duration: durée de la formation
    :return: Une structure de données représentant une formation
    """
    duration = int(duration)
    if duration < 1:
        raise ValueError("duration should be at least 1 (day)")

    return dict(subject=name, duration=duration, attendents=[])


def add_attendent(training: dict, name: str):
    """
    Ajoute un stagiaire à la formation

    :param training: une formation
    :param name: nom du stagiaire
    """
    training['attendents'].append(name)


def display_trainig(training):
    """
    Affiche le contenu d'une formation

    :param training: La formation à afficher
    """
    print("""
Formation "{}"
------------
Durée : {}
Participants : {}
    """.format(training['subject'], training['duration'], len(training['attendents'])))

    for attendent in training['attendents']:
        print(' - {}'.format(attendent))


if __name__ == '__main__':
    pass
