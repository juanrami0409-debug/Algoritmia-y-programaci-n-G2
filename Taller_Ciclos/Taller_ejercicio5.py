tanque_vacio = input("¿El detector del tanque vacio esta activado? (si/no): ")
if tanque_vacio.lower() == "si":
    print("Valvula abierta. Llenando el tanque...")
    tanque_lleno = input("¿El detector del tanque lleno esta activado? (si/no): ")
    if tanque_lleno.lower() == "si":
        print("Valvula cerrada. El tanque esta lleno.")
else:
    print("El tanque no nesesita llenar.")