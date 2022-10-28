def menu():
    print("************************")
    print("********  MENU  ********")
    print("************************")
    print("1. Ingresar dinero")
    print("2. Sacar dinero")
    print("3. Salir")
    print("")
def main():
    seguir = True
    saldo = 0
    while seguir == True:
        respuesta = int(input("¿Qué deseas hacer?: "))
        if respuesta == 1:
            saldo = ingresar_dinero(saldo)
            seguir = True
        elif respuesta == 2:
            if saldo == 0:
                print("No puedes sacar dinero.")
                print(f"Tienes 0€ en la cuenta.\n")
                seguir = True
            else:
                saldo = sacar_dinero(saldo)
                seguir = True
        elif respuesta == 3:
            print("Muchas gracias y hasta pronto.")
            seguir = False
        else:
            print("Este argumento no es válido.")
            menu()
            main()
def ingresar_dinero(saldo):
    dinero = int(input("¿Cuánto dinero quieres ingresar?: "))
    if dinero < 0:
        print("No puedes ingresar números negativos.")
        ingresar_dinero(saldo)
    else:
        saldo = saldo + dinero
        print(f"Tienes {saldo}€.\n")
        return(saldo)
def sacar_dinero(saldo):
    dinero = int(input("¿Cuánto dinero quieres sacar?: "))
    if dinero < 0:
        print("No puedes sacar números negativos.")
        sacar_dinero(saldo)
    elif dinero > saldo:
        print("No tienes tanto dinero.")
        print(f"Tienes {saldo}€ en la cuenta.")
        sacar_dinero(saldo)
    else:
        saldo = saldo - dinero
        print(f"Tienes {saldo}€.")
        print("")
        return(saldo)

menu()
main()
