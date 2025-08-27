def calculadora():
    Num1 = int (input("Primer Numero: "))
    Num2 = int (input("Segundo Numero: "))
    operacion = input("Elige una operación (+ - / x): ")

    if operacion == "+":
        print(Num1 + Num2)
    elif operacion == "-":
        print(Num1 - Num2)
    elif operacion == "/":
        if Num2 != 0:
            print(Num1 / Num2)
        else:
            print ("Error, no se puede dividir entre 0.")
    elif operacion == "x":
        print(Num1 * Num2) 
    else:
        print("Error, operacion Invalida digite (+ - / x)")
    return input("Quieres hacer otra operacion? (s/n)").lower()
while True:
    respuesta = calculadora()
    if respuesta != "s":
        print("Vayasealaverga")
        break