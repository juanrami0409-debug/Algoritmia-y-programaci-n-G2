Hora = input("ingrese la hora: ")
if Hora == "6:00":
    print("Alarma sonara por 1 minuto")
    apagar = input("¿Desea apagar la alarma? (si/no): ")
    if apagar.lower() == "si":
        print("Alarma apagada")
    else:
        print("Alarma seguirá sonando por 1 minuto")
else:
    print("No es hora de despertar")