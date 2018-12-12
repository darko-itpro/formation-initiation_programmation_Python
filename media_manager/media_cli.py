#!/usr/bin/env python

from media_manager import media as mm

movies_collection = mm.create_collection()


def add_movie(title=None):
    """
    Ajoute une information de film à la collection.

    La saisie incorrecte de la durée par l'utilisateur déclenchera une erreur
    lors de la conversion en entier. La gestion d'erreur proposerea à
    l'utilisateur de saisir à nouveau la durée ce qui provoquera le rappel de
    cette fonction. Le paramètre `title` permet de passer le titre déjà saisi à
    cette fonction pour éviter de lui demander de le saisir à nouveau.

    :param title: titre du film à ajouter, paramètre prévu pour l'appel de la
    gestion d'erreur.
    :return: None
    """
    print("-----")
    if title is None:
        print("Saisissez les informations sur le film")
        title = input("Titre du film : ")
    else:
        print("Saisissez la durée pour {}".format(title))
    try:
        duration = int(input("Durée du film : "))

        mm.add_movie(movies_collection, title, duration)
        print('Film ajouté\n')
    except ValueError:
        print(">>> La durée doit être un nombre <<<")
        retry = input("Réessayer ? (y/N)")
        if retry.lower() == "y":
            add_movie(title)


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