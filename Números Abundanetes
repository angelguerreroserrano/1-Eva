print("Un número abundante es todo aquel que sus divisores suman más que el propio número.")
print("Este programa te dice los números abundantes que hay hasta el número que pongas.")
limite = int(input("Introduce un número: "))
for j in range(1,limite + 1):
    suma_divisores = 0
    for i in range(j-1,0,-1):
        if j%i == 0:
            suma_divisores = suma_divisores + i
    if suma_divisores > j:
        print(j)
