
training_to_cancel = ["Python, initiation", 2, 1200, False]
training_to_maintain = ["Django, initiation", 4, 2200, True]

training = training_to_maintain
# training = training_to_cancel

if training[3]:
    print("Formation assurée")
else:
    print("Formation annulée")
