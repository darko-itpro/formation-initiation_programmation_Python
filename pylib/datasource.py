import random
random.seed()

bbt_s12 = [['The Conjugal Configuration', True, 20],
           ['The Wedding Gift Wormhole', True, 21],
           ['The Procreation Calculation', True, 20],
           ['The Tam Turbulence', True, 19],
           ['The Planetarium Collision', True, 19],
           ['The Imitation Perturbation', True, 19],
           ['The Grant Allocation Derivation', True, 19],
           ['The Consummation Deviation', True, 22],
           ['The Citation Negation', True, 20],
           ['The VCR Illumination', False, 20],
           ['The Paintball Scattering', False, 19],
           ['The Propagation Proposition', False, 20],
           ['The Confirmation Polarization', False, 20],
           ['The Meteorite Manifestation', False, 19],
           ['The Donation Oscillation', False, 21],
           ['The D & D Vortex', False, 20],
           ['The Conference Valuation', False, 19],
           ['The Laureate Accumulation', False, 21],
           ['The Inspiration Deprivation', False, 20],
           ['The Decision Reverberation', False, 19],
           ['The Plagiarism Schism', False, 19],
           ['The Maternal Conclusion', False, 20],
           ['The Change Constant', False, 19],
           ['The Stockholm Syndrome', False, 23]]

def time_loader():
    return "30"


def get_start_time():
    return "20h42"


def get_season(user=None):
    """
    Fonction permétant d'accéder à la saison d'une série. Si un paramètre user est passé, le retour
    sera adapté à l'utilisateur

    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par une liste
    [titre:str, vu:bool, durée:int]. Sinon, une liste de titres.
    """
    if user is None:
        return [title for title, *_ in bbt_s12]
    else:
        return bbt_s12


def _to_dict(title, duration, viewed):
    episode = {"title": title, "duration": duration}
    if viewed:
        episode['viewed'] = True
    else:
        if random.random() > 0.8:
            episode['viewed'] = False

    return episode

def load_season(user=None):
    return [_to_dict(title, duration, viewed)
            for title, viewed, duration in bbt_s12]


def get_movies():
    return [["The Philosopher's Stone", 152, True],
            ["The Chamber of Secrets", 161, True],
            ["The Prisoner of Azkaban", 142, False],
            ["the Goblet of Fire", 157, True],
            ["the Order of the Phoenix", 138, False],
            ["the Half-Blood Prince", 153, True],
            ["the Deathly Hallows – Part 1", 126, False],
            ["the Deathly Hallows – Part 2", 130, False]]


def get_stranger_code(as_dict=False):
    if as_dict:
        return [{'title': 'Installing the softwares',
                 'number': 1,
                 'duration': 42,
                 'viewed': 0},
                {'title': 'It works !', 'number': 2, 'duration': 51, 'viewed': 0},
                {'title': 'It does not work anymore',
                 'number': 3,
                 'duration': 47,
                 'viewed': 0},
                {'title': 'Launching the debug', 'number': 4, 'duration': 46, 'viewed': 0},
                {'title': 'Did someone read the doc ?',
                 'number': 5,
                 'duration': 42,
                 'viewed': 0},
                {'title': 'Trying that stuff from Stack Overflow…',
                 'number': 6,
                 'duration': 58,
                 'viewed': 0},
                {'title': 'The client wants a demo',
                 'number': 7,
                 'duration': 51,
                 'viewed': 0},
                {'title': 'Release Day !', 'number': 8, 'duration': 72, 'viewed': 0}]
    else:
        return [['Installing the softwares', 1, 42, 0],
                ['It works !', 2, 51, 0],
                ['It does not work anymore', 3, 47, 0],
                ['Launching the debug', 4, 46, 0],
                ['Did someone read the doc ?', 5, 42, 0],
                ['Trying that stuff from Stack Overflow…', 6, 58, 0],
                ['The client wants a demo', 7, 51, 0],
                ['Release Day !', 8, 72, 0]]
