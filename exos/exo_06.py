training_to_maintain = {"title": "Python, initiation",
                        "duration": 2,
                        "price": 1200,
                        "students": 5,
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

def is_maintained(training:dict) -> bool: # Pour vous, training a une clef "students"
    if "students" not in training:
        return False

    return bool(training["students"])


print(is_maintained(training_to_maintain))
print(is_maintained(training_to_cancel))
print(is_maintained(training_no_key))















