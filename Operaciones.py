# Para hacer operaciones
print (2+3)
print (2-3)
print (2*3)
print (2/3)

# a, b y c son variantes, que las defino al principio
a = 2
b = 3
c = a+b
print (c)

# También se puede sumar nombres, o multiplicarlos
a = Angel
b = Guerrero
print (a+b)
print (a*2)

# Varias operaciones
numero1 = int(input("Número 1: "))
print (f"Tú número es el {numero1}, ¿es correcto?")
print ("En caso de afirmación pon Sí, en caso de negación pon No")
si = input()
if si == "Sí":
    numero2 = int(input("Número 2: "))
    print (f"Tú número es el {numero2}, ¿es correcto?")
    print ("En caso de afirmación pon Sí, en caso de negación pon No")
si = input()
if si == "Sí":
    print (f"La suma es {numero1+numero2}")
    print (f"La resta es {numero1-numero2}")
    print (f"La multiplicación es {numero1*numero2}")
    print (f"La pontencia es {numero1**numero2}")
    print (f"La división es {numero1/numero2}")
    print (f"La división entera es {numero1//numero2}")
    print (f"El resto es {numero1%numero2}")
