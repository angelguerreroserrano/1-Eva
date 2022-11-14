# la función len() cuenta las letras que tiene una palabra

def detecta_tipo_letra(letra):
    respuesta = False
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        respuesta = True
    else:
        respuesta = False
    return (respuesta)

def deletreo():
    palabra = input("Dime una palabra: ")
    cuenta_vocales = 0
    cuenta_consonantes = 0
    for cont in range(0,len(palabra)):
        print (palabra[cont])
        if detecta_tipo_letra(palabra[cont]) == True:
            cuenta_vocales = cuenta_vocales + 1
        else:
            cuenta_consonantes = cuenta_consonantes + 1
    print(f"La palabra tiene {cuenta_vocales} vocales")
    print(f"La palabra tiene {cuenta_consonantes} consonantes.")

deletreo()
