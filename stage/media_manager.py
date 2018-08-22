#!/usr/bin/env python


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
    collection.append([title, duration, viewed])
    return collection


def time_remaining(collection):
    """
    Retourne la durée totale des films restant à voir dans la collection.

    :param collection: une liste de films
    :type collection: list
    :return: la durée restant à voir
    :rtype: int
    """
    return sum([time for title, time, viewed in collection if not viewed])


if __name__ == '__main__':
    pass