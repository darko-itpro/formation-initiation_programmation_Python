#!/usr/bin/env python 
# -*- coding: utf-8 -*-

LOW = 0
MEDIUM = 1
HIGH = 2


def add_to(collection, title, priority=0):
    """
    Ajoute une tâche à une liste de tâches.

    :param collection: une liste de tâches
    :type collection: list
    :param title: titre de la tâche
    :param priority: priorité représentée sous la forme d'un entier de 0 à 2
    :return: la liste de tâches
    """
    collection.append([title, priority, False])
    return collection


def next_item(collection, highest_priority=True):
    selected_task = None
    selected_priority = -1
    for task, priority, done in collection:
        if not done and priority > selected_priority:
            selected_priority = priority
            selected_task = task
            if not highest_priority:
                break

    return [selected_task,
            selected_priority] if selected_priority >= 0 else None


def mark_as_done(collection, task):
    for item in collection:
        if item[0] == task:
            item[2] = True
            break
    return collection
