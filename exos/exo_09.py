import copy

training = {"title":"Python, les fondamentaux",
            "duration": 5,
            "max_students": 8,
            "students": [],
           }

second_training = copy.deepcopy(training)

def add_student(training:dict, student:dict):
    training["students"].append(student)

add_student(training, {"name":"John"})
add_student(second_training, {"name":"Ballerina"})
print(id(training) == id(second_training))
print(training is second_training)

print(training)
