import random

x = 0
y = 0

pasos = 0

while pasos < 100:

    direccion = random.randint(1,4)

    if direccion == 1:
        x = x + 1

    elif direccion == 2:
        x = x - 1

    elif direccion == 3:
        y = y + 1

    else:
        y = y - 1

    pasos = pasos + 1

print("Ubicación final:", x, y)