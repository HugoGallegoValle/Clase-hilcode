# Escribe tu código aquí :-)
#funciones
def par_o_impar():
    numero = int(input("Escribe un número"))
    if numero % 2 == 0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")
par_o_impar()
#utilizar la variable fuera de la función
def par_o_impar1():
    numero = int(input("Escribe un número"))
    if numero % 2 == 0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")
    return numero
numero = par_o_impar1(numero)
print("El número es :",numero)
#utilizar variables en funciones desde fuera
def par_o_impar(numero):
    if numero % 2 == 0:
        print("El número",numero,"es par")
    else:
        print("El número",numero,"es impar")
numero = input(int("Escribe un número")
par_o_impar(numero=numero)
