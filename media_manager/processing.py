#!/usr/bin/env python

"""
Module de gestion des données par listes
"""


def create_collection():
    """
    Crée une nouvelle collection vide.

    Cette méthode retourne une liste car c'est sous forme de ce type que ce
    module gère les collections.
    :return: une nouvelle collection vide
    """
    return list()


def add_movie(collection, title, duration=None, viewed=False):
    """
    Ajoute les information d'un film à la collection

    :param collection: une liste de films
    :type collection: list
    :param title: le titre du film
    :param duration: la durée du film en minutes
    :param viewed: indique si le film a été vu ou non
    :type viewed: bool
    :return: la collection de films avec le film ajouté
    """
    if title in [media[0] for media in collection]:
        raise ValueError("Media already in collection")

    collection.append([title, duration, viewed])
    return collection


def set_as_viewed(collection, title):
    """
    Change le statut vu d'un média, implémentation par recherche d'élément

    :param collection: une liste de médias
    :param title: le titre à mettre à jour
    :return: la collection des médias
    """
    for movie in collection:
        if title == movie[0]:
            movie[2] = True
            break
    else:
        raise ValueError('Movie [{}] not in collection'.format(title))

    return collection


def set_as_viewed_v2(collection, title):
    """
    Change le statut vu d'un média, implémentation par recherche d'indice de
    l'élément

    :param collection: une liste de médias
    :param title: le titre à mettre à jour
    :return: la collection des médias
    """
    try:
        media_index = [media[0] for media in collection].index(title)
    except ValueError:
        raise ValueError('Movie [{}] not in collection'.format(title))
    collection[media_index][2] = True

    return collection


def time_remaining(collection):
    """
    Retourne la durée totale des films restant à voir dans la collection.

    :param collection: une liste de films
    :type collection: list
    :return: la durée des média restant à voir
    :rtype: int
    """
    return sum([time
                for title, time, viewed in collection
                if not viewed])
