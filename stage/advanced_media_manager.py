#!/usr/bin/env python


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
    :return: la collection de films avec le film ajouté
    """
    if title in collection:
        raise ValueError("Media already in collection")

    collection[title] = [title, duration, viewed]
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
                for title, time, viewed in list(collection.values())
                if not viewed])


if __name__ == '__main__':
    pass
