
training_to_cancel = ["Python, initiation", 2, 1200, 0]
training_to_maintain = ["Python, les fondamentaux", 5, 2600, 4]

def is_maintained(training:list):
    result = False
    if training[3]:
        result = True

    return result


def is_maintained(training: list) -> bool:
    return bool(training[3])


is_maintained(training_to_cancel)
is_maintained(training_to_maintain)