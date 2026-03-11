print("Candidatos disponibles:")
print("A - Partido Amarillo")
print("M - Partido Morado")
print("N - Partido Naranja")
opcion = input("Elija un candidato (A/M/N): ")
if opcion.upper() == "A":
    print("Usted ha elegido al Partido Amarillo")
elif opcion.upper() == "M":
    print("Usted ha elegido al Partido Morado")
elif opcion.upper() == "N":
    print("Usted ha elegido al Partido Naranja")
else:
    print("Opción no válida")