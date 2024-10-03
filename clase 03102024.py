# Escribe tu código aquí :-)
aciertos = 0
def funcion(aciertos):
    import random
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    resultado = num1*num2
    print("Cuánto es",num1,"X",num2)
    respuesta = int(input("Resultado:"))
    if respuesta == resultado:
        print("Correcto")
        aciertos = aciertos + 1
    else:
        print("Error vuelve a intentarlo")
    return aciertos
for pruebas in range(0,10):
    aciertos=funcion(aciertos)
print("Has acertado",aciertos,"/10")
