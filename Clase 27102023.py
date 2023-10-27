# Escribe tu código aquí :-)
'''
alumnos = []
tam = len(alumnos)
while len(alumnos)<5:
    alumnos.append(input("¿Cuál es l nombre del alumno?"))
print(alumnos)
'''
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
