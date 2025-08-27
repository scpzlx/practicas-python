def verficar_edad():
    edad=int( input("ingrese la edad para verficar si es mayor de edad:"))
    if edad >= 18:
        print(" ya caduco")
    else:
        print("tick tack tick tack")
    return input("Quieres probar otra edad? (s/n)").lower()
while True: 
    respuesta = verficar_edad()
    if respuesta != "s":
        print("abueno vayase alavrga")
        break