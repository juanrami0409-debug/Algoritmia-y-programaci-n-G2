import random
x = 0
y = 0
for i in range(10):
    dado = random.randint(1, 4)
    if dado == 1:
        x += 1
        print("Dado 1: Avanza a la derecha")
    elif dado == 2:
        x -= 1
        print("Dado 2: Avanza para abajo")
    elif dado == 3:
        y += 1
        print("Dado 3: Avanza hacia arriba")
    elif dado == 4:
        y -= 1
        print("Dado 4: Avanza hacia izquierda")
print(f"Posición final: ({x}, {y})")
print("pocisión final: ", (x, y))
