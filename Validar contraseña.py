def prueba_palabras():
    contraseña = input("Introduce una contraseña: ")
    if contraseña.islower() or contraseña.isupper():
        print("No cumple el criterio de tener mayúsculas y minúsculas")
    else:
        print("Sí cumple el criterio de tener mayúsculas y minúsculas")
        
prueba_palabras()

# otro
password = input("Introduce tu contraseña: ")
def main(password):
    tiene_simbolos(password)
    # tiene_numeros_letras(password)
    # tine_mayus_minus(password)
    # final_password(password)
    
def tiene_simbolos(password):
    if password.isalnum() == False:
        print("Tiene carácteres")
    else:
        print("No tiene carácteres")
        
main(password)
