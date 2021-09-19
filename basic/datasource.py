def time_loader():
    return "30"


def get_start_time():
    return "20h42"


def get_season(user=None):
    if user is None:
        return ["The Conjugal Configuration",
                "The Wedding Gift Wormhole",
                "The Procreation Calculation",
                "The Tam Turbulence",
                "The Planetarium Collision",
                "The Imitation Perturbation",
                "The Grant Allocation Derivation",
                "The Consummation Deviation",
                "The Citation Negation",
                "The VCR Illumination",
                "The Paintball Scattering",
                "The Propagation Proposition",
                "The Confirmation Polarization",
                "The Meteorite Manifestation",
                "The Donation Oscillation",
                "The D & D Vortex",
                "The Conference Valuation",
                "The Laureate Accumulation",
                "The Inspiration Deprivation",
                "The Decision Reverberation",
                "The Plagiarism Schism",
                "The Maternal Conclusion",
                "The Change Constant",
                "The Stockholm Syndrome"]

    else:
        return [['The Conjugal Configuration', True],
                ['The Wedding Gift Wormhole', True],
                ['The Procreation Calculation', True],
                ['The Tam Turbulence', True],
                ['The Planetarium Collision', True],
                ['The Imitation Perturbation', True],
                ['The Grant Allocation Derivation', True],
                ['The Consummation Deviation', True],
                ['The Citation Negation', True],
                ['The VCR Illumination', False],
                ['The Paintball Scattering', False],
                ['The Propagation Proposition', False],
                ['The Confirmation Polarization', False],
                ['The Meteorite Manifestation', False],
                ['The Donation Oscillation', False],
                ['The D & D Vortex', False],
                ['The Conference Valuation', False],
                ['The Laureate Accumulation', False],
                ['The Inspiration Deprivation', False],
                ['The Decision Reverberation', False],
                ['The Plagiarism Schism', False],
                ['The Maternal Conclusion', False],
                ['The Change Constant', False],
                ['The Stockholm Syndrome', False]]


def get_movies(serie, with_info=False):
    if not with_info:
        return [["The Philosopher's Stone", True],
                ["The Chamber of Secrets", True],
                ["The Prisoner of Azkaban", False],
                ["the Goblet of Fire", True],
                ["the Order of the Phoenix", False],
                ["the Half-Blood Prince", True],
                ["the Deathly Hallows – Part 1", False],
                ["the Deathly Hallows – Part 2", False]]
    else:
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
