#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from stage import task_manager as tm

tasks = []


def add_task():
    title = input("Titre de la tâche ")
    priority = int(input("Priorité de la tâche "))

    tm.add_to(tasks, title, priority)


def next_task():
    n_task = tm.next_item(tasks)
    if n_task:
        print("Prochaine tâche :", n_task[0])
    else:
        print('Plus de tâche')


while True:
    actions = {'a': add_task,
               'n': next_task}

    print("""Options:
    [a] ajouter une tâche
    [n] afficher tâche suivante
    [q] quit""")
    choice = input('Votre choix ? ')

    if choice == 'q':
        break
    elif choice in actions:
        actions[choice]()
    else:
        print('Choix non disponible')

print('Bye')