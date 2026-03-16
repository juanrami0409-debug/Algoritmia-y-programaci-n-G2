print("MENU EJERCICIO 2")
print("1. Suma de números pares entre 2 y 100")
print("2. Suma de cuadrados entre 1 y 100")
print("3. Suma de números impares entre a y b")
print("4. Suma de dígitos impares de un número")

opcion = int(input("Seleccione una opción: "))


if opcion == 1:

    suma = 0
    i = 2

    while i <= 100:
        suma = suma + i
        i = i + 2

    print("La suma es:", suma)


elif opcion == 2:

    suma = 0
    i = 1

    while i <= 100:
        suma = suma + i*i
        i = i + 1

    print("La suma de los cuadrados es:", suma)


elif opcion == 3:

    a = int(input("Ingrese el número a: "))
    b = int(input("Ingrese el número b: "))

    suma = 0

    while a <= b:

        if a % 2 != 0:
            suma = suma + a

        a = a + 1

    print("La suma de impares es:", suma)


elif opcion == 4:

    n = int(input("Ingrese un número: "))
    suma = 0

    while n > 0:

        digito = n % 10

        if digito % 2 != 0:
            suma = suma + digito

        n = n // 10

    print("La suma de los dígitos impares es:", suma)


else:
    print("Opción no válida")