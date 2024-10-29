training_to_cancel = ["Python, initiation", 2, 1200, 0]
training_without_students = ["Django, initiation", 4, 2200]

def is_maintained(training: list) -> bool:
    return bool(len(training) >= 4 and training[3])

print(is_maintained(training_to_cancel))
print(is_maintained(training_without_students))

def has_enough_data(training):
    return len(training) >= 4

def has_students(training):
    return bool(training[3])

def is_maintained(training: list) -> bool:
    return has_enough_data(training) and has_students(training)
