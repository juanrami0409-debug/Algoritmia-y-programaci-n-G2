num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación a realizar (+,-,*,/): ")
if operacion == "+":
    resultado = num1 + num2
    print("El resultado es:", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("El resultado es:", resultado)
elif operacion == "*":
    resultado = num1 * num2
    print("El resultado es:", resultado)
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")