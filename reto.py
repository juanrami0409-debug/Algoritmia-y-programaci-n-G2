#En una empresa se nesecita registrar la entrada y salida de sus trabajadore
#que esta compuesto por una coleccion de cinco personas, en caso de que una persona
#no sea parte de la base de datos mandar un mensaje de rechazo a la entrada.
trabajadores={"juan","maria","pedro","luis","ana"}
i=input("ingrese la hora de entrada: ")
n=input("Ingrese su nombre: ")
if n in trabajadores:
    print("Bienvenido")
else:
    print("Ni trabaja aqui muevase")
if trabajadores>0:
m=input("Ingrese la hora de salida: ")
if m in trabajadores:
    print("Hasta luego")
else:
    print("Y tu como entraste")
