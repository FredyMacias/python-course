x = 150000
y = 50000
z = 5000

print("\t:.MENÚ:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opción de menú:  "))

print()

if opcion==1:
    extra = float(input("Cuanto dinero desea ingresar"))
    x += extra
    print("Dinero en la cuenta: {x}")
elif opcion==2:
    retirar = float(input("Cuanto dinero desea retirar"))
    if retirar>x:
        print("No tiene esa cantidad de dinero")
    else:
        x -= retirar
        print("Dinero en la cuenta: {x}")
elif opcion==3:
    print("Dinero en la cuenta: {x}")
elif opcion==4:
    print("Gracias por utilizar su cajero automático")
else:
    print("Error, se equivocó de opción de menú")
    