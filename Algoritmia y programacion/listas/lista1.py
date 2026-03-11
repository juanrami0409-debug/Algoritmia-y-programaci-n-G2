#Una empresa de transporte tiene una lista con los nombres de sus conductores.
#Se pide realizar un programa que permita ingresar el nombre de un conductor y 
# verificar si se encuentra en la lista.
Conductores={"juan","maria","pedro","luis","sara"}
n=input("Ingrese su nombre: ")
if n in Conductores:
    print("El conductor se encuentra en la lista.")
else:
    print("El conductor no se encuentra en la lista.")
