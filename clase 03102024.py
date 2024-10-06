# Escribe tu código aquí :-)
aciertos = 0
ronda = 0
for intentos in range(0,15):
    import random
    if intentos == 0:
        print("En la primera ronda conseguirás 1 punto por acierto, el rango será del 1 al 10")
        ronda = 1
    if intentos == 5:
        print("En la segunda ronda conseguirás 2 puntos por acierto, el rango será del 5 al 15")
        ronda = 2
    if intentos == 10:
        print("En la tercera ronda conseguirás 3 puntos por acierto, el rango será del 10 al 20")
        print("¡Ten cuidado¡ en esta última ronda pierdes 1 punto por fallo")
        ronda = 3
    if intentos < 5:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        resultado = num1*num2
    if intentos < 10 and intentos > 4:
        num1 = random.randint(5,15)
        num2 = random.randint(5,15)
        resultado = num1*num2
    if intentos < 15 and intentos > 9:
        num1 = random.randint(10,20)
        num2 = random.randint(10,20)
        resultado = num1*num2
    print("Cuánto es",num1,"X",num2)
    respuesta = int(input("Resultado:"))
    if respuesta == resultado:
        print("Correcto")
        if ronda == 1:
            aciertos = aciertos + 1
        if ronda == 2:
            aciertos = aciertos + 2
        if ronda == 3:
            aciertos = aciertos + 3
    else:
        print("Error")
        if ronda == 3:
            aciertos = aciertos - 1
            print("-1 punto")
print("Tienes",aciertos,"puntos")
