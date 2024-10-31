
training_to_cancel = ["Python, initiation", 2, 1200, 0]
training_to_maintain = ["Python, les fondamentaux", 5, 2600, 4]

def is_maintained(training:list) -> bool:
    return bool(training[3])

print(is_maintained(training_to_maintain))
print(is_maintained(training_to_cancel))
