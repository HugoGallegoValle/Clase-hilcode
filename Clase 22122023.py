# Escribe tu código aquí :-)
import random
'''
def pedir_num() :
    secret = int(input("¿Qué número quieres que el otro adivine?"))
    return secret
secret = pedir_num()
def comparación (secret):
continuación = True
    while continuación:
        respuesta = int(input("Intenta adivinar el número"))
        if respuesta < secret:
            print("El número es mayor")
        elif respuesta > secret:
            print("El núemro es menor")
        else:
            print("¡¡¡Lo has consegudo¡¡¡")
            continuación = False
comparación(secret)
'''
#con aleatorio
def pedir_num() :
    secret = random.randint(0,100)
    return secret
secret = pedir_num()
def comparación (secret):
    continuación = True
    while continuación:
        respuesta = int(input("Intenta adivinar el número"))
        if respuesta < secret:
            print("El número es mayor")
        elif respuesta > secret:
            print("El núemro es menor")
        else:
            print("¡¡¡Lo has consegudo¡¡¡")
            continuación = False
comparación(secret)
