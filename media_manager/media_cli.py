#!/usr/bin/env python

from media_manager import processing as mm

movies_collection = mm.create_collection()


def add_movie():
    print("-----")
    print("Saisissez les informations sur le film")
    title = input("Titre du film : ")
    duration = int(input("Durée du film : "))

    mm.add_movie(movies_collection, title, duration)
    print('Film ajouté\n')


def remaining_time():
    total_time = mm.time_remaining(movies_collection)
    hours_remaining, minutes_remaining = divmod(total_time, 60)
    print("-----")
    # ci-dessous, {:02}, 0 est le caractère de remplissage
    print("Vous avez {:2}h{:02} de films à regarder".format(hours_remaining,
                                                           minutes_remaining))


while True:
    actions = {'a': add_movie,
               't': remaining_time}

    print("""Options:
    [a] ajouter un film
    [t] afficher la durée restante
    [q] quit""")
    choice = input('Votre choix ? ')

    if choice == 'q':
        break
    elif choice in actions:
        actions[choice]()
    else:
        print('Choix non disponible')

print('Bye')