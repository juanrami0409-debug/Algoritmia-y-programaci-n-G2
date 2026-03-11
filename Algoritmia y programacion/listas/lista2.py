#Una empresa de energía quiere llevar un registro de sus clientes y su consumo
#de energía. Se pide realizar un programa que permita ingresar el nombre del 
#cliente y su consumo en kWh, y luego calcular el costo total a pagar considerando
#que el precio por kWh es de $0.15.
Clientes={}
n=input("Ingrese el nombre del cliente: ")
c=float(input("Ingrese el consumo en kWh: "))
Clientes[n]=c
precio=0.15
costo_total=Clientes[n]*precio
print("El costo total a pagar por el cliente", n, "es: $", costo_total)