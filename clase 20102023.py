# Escribe tu código aquí :-)
'''qqa
dinero = float(input("Cuánto dienro tienes"))
chuche = 1
pastel = 3.5
pan = 0.85
nocilla = 3.5
compra = chuche + pastel + pan + nocilla
print("El total de la compra es de",compra,"€")
if dinero >= compra:
    print("Compra aceptada.\n Tienes ahora",dinero-compra,"€")
else:
    print("Trajeta denegada")
    print("Te faltan:", compra - dinero,"€")
    '''

#mi programa
'''
masclassnum = 16
usarameclassnum =  int(input("¿Cuántos alumnos y alumnas hay en tu clase?"))
if masclassnum >= usarameclassnum:
    print("Tu clase tiene un número correcto de alumnos/as")
else:
    print("Tu clase es demasiado grande")
    print("necesitas",usarameclassnum - masclassnum,"alumnos/as menos")


#programa corregido auque el otro est bien este es más extenso y preferible
alumnos = []
aula = 10
alumnos.append(input("¿Cuaál es el nombre del alumno?"))
alumnos.append("¿Cuaál es el nombre del alumno?")
alumnos.append("¿Cuaál es el nombre del alumno?")
if len(alumnos) > aula:
    print("No hay espacio suficiente, no pases")
else:
    print("Vale podéis entrar")

    '''
##################################################################################
num = int(input("Número"))
if num >50:
    print("El número es mayor que 50")
elif num == 50:
    print("El número es 50")
elif num < 50:
    print("El número es menor de 50")
elif num < 50 or num == 50:
    print("El número es igual de 50")
elif num > 50 or num == 50:
    print("El número es menor oigual de 50")
elif num > 50 or num== 50:
    print("El número es mayor o igual que 50")
else:
    print("Qué número?????")

if num > 50 and num < 100:
    print("El número está entre 50 y 100")
elif num < 50 or num > 100:
    print("El número no está entre 50 y 100")
else:
    print("El número o es 50 o es 100")
