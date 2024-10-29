training_to_maintain = {"title": "Python, initiation",
                        "duration": 2,
                        "price": 1200,
                        "students": 3,
                        }
training_to_cancel = {"title": "Python, les fondamentaux",
                      "duration": 5,
                      "price": 2600,
                      "students": 0,
                      }
training_no_key = {"title": "Django, initiation",
                   "duration": 4,
                   "price": 2200,
                   }

def is_maintained(training:dict, min_students:int = 1):
    return bool("students" in training and training["students"] >= min_students)

print(is_maintained(training_to_maintain, 6))
print(is_maintained(training_to_maintain))
print(is_maintained(training_to_cancel))
print(is_maintained(training_no_key))


def is_maintained(training:dict, cost:float=None):
    if cost is None:
        return True

    return bool("students" in training and (training["students"] * training['price']) >= cost * 1.1 )

print(is_maintained(training_to_maintain, 2000))
print(is_maintained(training_to_maintain, 4000))

