from faker import Faker
from random import randint

def get_students():
    """
    Produit une liste (aléatoire) de stagiaires (entre 4 et 25)

    :return: Une liste de participants sous forme de dictionnaire avec clefs `name` et `company`.
    """
    fake = Faker('fr_FR')
    return [{'name': fake.name(), 'company': fake.company()}
            for i in range(randint(4, 25))
            ]
