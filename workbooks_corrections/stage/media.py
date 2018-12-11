#!/usr/bin/env python 

"""
Module de démonstration des imports dans les notebooks
"""


def add_media(collection, title, year, duration, viewed):
    """
    Ajoute un media à la collection

    :param collection: La collection de medias
    :param title: titre du média
    :param year: année du média
    :param duration: durée du média
    :param viewed: indicateur que le média a été vu
    :return: la collection avec le média ajouté
    """
    collection.append([title, year, duration, viewed])
    return collection


my_collection = []
print(len(my_collection))

add_media(my_collection, "The Philosopher's Stone", 2001, 152, False)
print(my_collection)
