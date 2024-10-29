# Correction de l'exercice sur les boucles

# Déclaration des éléments immuables : liste des inscrits et fonction.

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


def add_student(training:dict, student:dict):
    training["students"].append(student)


# Première question
# Déclaration de la formation
first_training = {"title":"Python, les fondamentaux",
                  "duration": 5,
                  "max_students": 8,
                  "students": [],
                 }

for student in students:
    add_student(first_training, student)

# Affichage de la taille de la liste des stagiaires de la formation pour valider son remplissage
print(len(first_training['students']))

# Second exercice
# Déclaration de la formation pour la réinitialiser
first_training = {"title":"Python, les fondamentaux",
                  "duration": 5,
                  "max_students": 8,
                  "students": [],
                 }

# Le principe va être d'itérer sur les inscrits pour les affecter à la formation. Mais nous allons
# tester si des places sont encore disponibles et si non, interrompre l'itération avec break.
for student in students:
    add_student(first_training, student)
    if len(first_training["students"]) >= first_training["max_students"]:
        break

# Affichage de données dont le premier et dernier inscrit pour validation.
print(len(first_training))
print(first_training["students"][0]["name"])
print(first_training["students"][-1]["name"])

# On recrée la formation pour le troisième exercice
# Déclaration de la formation pour la réinitialiser
first_training = {"title":"Python, les fondamentaux",
                  "duration": 5,
                  "max_students": 8,
                  "students": [],
                 }

# Déclaration de la liste d'attente avec une liste vide.
wait_list = []
# L'itération est identique à la précédente mais on utilise enumerate pour récupérer l'indice
# qui servira à construire la liste d'attente
for index, student in enumerate(students):
    add_student(first_training, student)
    if len(first_training["students"]) >= first_training["max_students"]:
        # La liste d'attente est créée en faisant un slice à partir de l'élément après le dernier inscrit
        wait_list = students[index + 1:]
        break

# La liste des inscrits sera la même que l'exercice précédent, voici la liste d'attente.
print(wait_list)
