saldo = 150000
billete = 100000
billete1 = 50000

print(".:MENU:.")
print("1. Ingresar dinero")
print("2. Retirar dinero")
print("3. Salir")
opcion = int(input("Digite una opción de menú:  "))

print()

if opcion==1:
    extra = float(input("Cuanto dinero desea ingresar"))
    saldo = saldo + extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==2:
    retirar = float(input("Cuanto dinero desea retirar"))
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    if retirar<saldo:
        print(f"Dinero en la cuenta: {saldo - retirar}")
    if retirar==saldo:
        print("Recibe 100000 + 50000")
elif opcion==3:
    print("Gracias por utilizar su cajero automático")
else:
    print("Error, se equivocó de opción de menú")