# Escribe tu código aquí :-)

alumnos = []
tam = len(alumnos)
while len(alumnos)<5:
    alumnos.append(input("¿Cuál es l nombre del alumno?"))
print(alumnos)

#pogrma mio (anterior
numsecret = int(input("Elige un número"))
print("Escribe un número entre 0 y 15")
estado = True
while estado:
    numusurame=int(input("¿Qué número estoy pensando?"))
    if numsecret == numusurame:
        print("Has acertado")
        estado = False
    elif numusurame > numsecret:
        print("El número que el oredenador esta pensando es menor")
    else:
        print("El número que el ordenador esta pensando es mayor")

#programa de manera más corta
numero = int(input("Elige un número: "))
respuesta = int(input("¿Ahora tienes que intentar acertar el número: "))
while respuesta != numero:
    if respuesta > numero:
        print("Tu numero es mayor del numero correcto")#
    elif respuesta < numero:
        print("Tu numero es menor que el número correcto")
    respuesta = int(input("Ahora tienes que intentar acertar el número"))
print("El número es el correcto")

#otra manera de hacerlo
numero = int(input("Elige un número"))
fin = False
while not fin:
    respuesta = int(input("Elige un numero"))
    if respuesta > numero:
        print("Tu numero es mayor del numero correcto")#
    elif respuesta < numero:
        print("Tu numero es menor que el número correcto")
    else:
        fin = True
print("El número es el correcto")
