# Escribe tu código aquí :-)
#ordenador adivina inteligentemente
calculo = 0
bucle = 1
maximo = 101
minimo = 0
secret = int(input("Escribe un número del 1 al 100 para que el ordenador lo adivine"))
while bucle == 1:
    calculo = (maximo+minimo)//2
    print(calculo)
    if calculo == secret:
        print("El número era",calculo)
        bucle = 0
    elif calculo < secret:
        minimo = calculo
    else:
        maximo = calculo
#Aleatorio
import random
calculo = 0
bucle = 1
maximo = 101
minimo = 0
secret = int(input("Escribe un número del 1 al 100 para que el ordenador lo adivine"))
while bucle == 1:
    calculo = random.randint(0,101)
    print(calculo)
    if calculo == secret:
        print("El número era",calculo)
        bucle = 0
    elif calculo < secret:
        minimo = calculo
    else:
        maximo = calculo
