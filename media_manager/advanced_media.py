#!/usr/bin/env python

"""
Module proposant une gestion des données par dictionnaires
"""


def create_collection():
    """
    Crée une nouvelle collection vide.

    Cette méthode retourne un dictionnaire car c'est sous forme de ce type que
    ce module gère les collections.
    :return: une nouvelle collection vide
    """
    return dict()


def add_movie(collection, title, duration=None, viewed=False):
    """
    Ajoute les information d'un film à la collection

    :param collection: une liste de films
    :type collection: dict
    :param title: le titre du film
    :param duration: la durée du film en minutes
    :param viewed: indique si le film a été vu ou non
    :type viewed: bool
    """
    if title in collection:
        raise ValueError("Media already in collection")

    collection[title] = dict(duration=duration, viewed=viewed)


def set_as_viewed(collection, title):
    if title not in collection:
        raise ValueError('Movie [{}] not in collection'.format(title))

    collection[title]["viewed"] = True


def time_remaining(collection):
    """
    Retourne la durée totale des films restant à voir dans la collection.

    :param collection: une liste de films
    :type collection: list
    :return: la durée des média restant à voir
    :rtype: int
    """
    return sum([time
                for title, time, viewed in list(collection.values())
                if not viewed])
