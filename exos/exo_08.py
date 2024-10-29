students = [{'name': 'Éric de Voisin', 'company': 'Petitjean Bonnet et Fils'},
            {'name': 'Richard Lamy', 'company': 'Bertin SA'},
            {'name': 'Auguste Jourdan-Hernandez', 'company': 'Nguyen'},
            {'name': 'Antoine Gaudin', 'company': 'Fournier'},
            {'name': 'Capucine Bonnin du Bourgeois', 'company': 'Pelletier'},
            {'name': 'Denise Rocher', 'company': 'Gosselin Boyer et Fils'},
            {'name': 'Édouard Le Goff', 'company': 'Lemaire'},
            {'name': 'Simone Chartier de la Richard', 'company': 'Bazin'},
            {'name': 'Dominique Langlois', 'company': 'Chevallier'},
            {'name': 'Denis-Roger Blot', 'company': 'Albert et Fils'},
            {'name': 'Jacques Rousset', 'company': 'Devaux SARL'},
            {'name': 'Georges Ledoux', 'company': 'Benard'},
            {'name': 'Louise Maillet Le Maury', 'company': 'Auger Ruiz S.A.R.L.'},
            {'name': 'Audrey Martin', 'company': 'Rocher Daniel S.A.'},
            {'name': 'Frédéric Diaz-Pons', 'company': 'Lacombe'},
            {'name': 'Patricia-Alexandria Maréchal', 'company': 'Leleu'},
            {'name': 'Émile Cohen', 'company': 'Poirier et Fils'},
            {'name': 'Maurice Evrard', 'company': 'Guilbert'},
            {'name': 'Adélaïde Morel du Germain', 'company': 'Bigot'},
            {'name': 'Marc Roche', 'company': 'Pages S.A.'}]


def get_participants(registered:list, max_seats:int):
    return registered[:max_seats], registered[max_seats:]

print(get_participants(students, 12))
print(get_participants(students[:10], 12))