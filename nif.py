def NIF():
    nif = input("Introduce el NIF (xxxxxxxx-x): ")
    if nif[8:9] != "-":
        print("No has seguido el formato (xxxxxxxx-x).")
        NIF()
    else:
        num_nif = int(nif[0:-2])
        letra_nif = str(nif[9:])
        numero = num_nif%23
        letras = "TRWAGMYFPDXBNJZSWVHLCKE"
        l_nif = letras[numero:(numero+1)]
        if l_nif != letra_nif:
            print("El número o la letra es incorrecto")
        else:
            print("Tu NIF es correcto")

x = True
while x == True:
    NIF()
    x = True
