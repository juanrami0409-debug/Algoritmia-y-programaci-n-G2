print("MENU")
print("1. Cuadrados menores que n")
print("2. Numeros divisibles por 10 menores que n")
print("3. Potencias de 2 menores que n")

opcion = int(input("Ingrese una opcion: "))
n = int(input("Ingrese un numero: "))

if opcion == 1:
    i = 1
    while i*i < n:
        print(i*i)
        i += 1

elif opcion == 2:
    i = 10
    while i < n:
        print(i)
        i += 10
elif opcion == 3:
    potencia = 1
    while potencia < n:
        print(potencia)
        potencia = potencia * 2
else:    print("Opcion no valida")