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


def add_movie(collection, title, duration, viewed):
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
    pass


def time_remaining(collection):
    """
    Retourne la durée totale des films restant à voir dans la collection.

    :param collection: une liste de films
    :type collection: list
    :return: la durée des média restant à voir
    :rtype: int
    """
    pass
