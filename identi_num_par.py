def par_inpar(): 
    numero = int ( input("ingresa un numero par: "))
    if numero % 2 == 0:
        print (f"si el numero {numero} es par")
    else :
        print (f"No, el numero {numero} no es par")
    return input("Quieres verificar otro numero (s/n)?: ").lower()
while True:
    respuesta = par_inpar()
    if respuesta != "s":
        print("a bueno vtalaverg")
        break