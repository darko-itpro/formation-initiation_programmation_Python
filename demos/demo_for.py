
camelot = ["Arthur", "Merlin", "Lancelot", "Robin", "Perceval", "Karadoc"]

for knight in camelot:
    print(knight.upper())

for index, knight in enumerate(camelot):
    if index % 2:
        print(" >", knight)
    else:
        print(' -', knight)

for i in range(4):
    print("turn left")
