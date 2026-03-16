print("MENU EJERCICIO 3")
print("1. Mostrar potencias de 2 desde 2^0 hasta 2^20")
print("2. Mostrar potencias de 3 desde 3^0 hasta 3^10")
print("3. Mostrar potencias de 5 desde 5^0 hasta 5^8")

opcion = int(input("Seleccione una opción: "))


if opcion == 1:

    i = 0
    while i <= 20:
        print("2^", i, "=", 2**i)
        i = i + 1


elif opcion == 2:

    i = 0
    while i <= 10:
        print("3^", i, "=", 3**i)
        i = i + 1


elif opcion == 3:

    i = 0
    while i <= 8:
        print("5^", i, "=", 5**i)
        i = i + 1


else:
    print("Opción no válida")