# Escribe tu código aquí :-)
#funciones
'''
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
par_o_impar(numero)
#tupla
tupla = (1,2,3)
'''
#actividad
def suma (num1, num2) :
    resultado = num1 + num2
    return resultado
resultado = suma(num1= 9, num2 = 10)
print("La suma da",resultado)
#resta
def resta (num1, num2) :
    resultado1 = num1 - num2
    return resultado1
resultado1 = resta(num1 = 9, num2 = 10)
print("La resta da",resultado1)
#multiplicación
def multiplicacion (num1, num2) :
    resultado2 = num1 * num2
    return resultado2
resultado2 = multiplicacion(num1 = 9, num2 = 10)
print("La multiplicación da",resultado2)
#division
def division (num1, num2) :
    resultado3 = num1 / num2
    return resultado3
resultado3 = division(num1 = 9, num2 = 10)
print("La division da",resultado3)
