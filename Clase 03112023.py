# Escribe tu código aquí :-)
'''
alumnos = []
for cantidad in range(5):
    alumnos.append(input("¿Cuál es el nombre del alumno?"))
print(alumnos)
#programa mio
total = 0
for cantidad in range(101):
    total= cantidad + total
print("El total es de",total)

#programa piedra papel o tijeras
puntosjugador1 = 0
puntosjugador2 = 0
empate = 0
continuación = True
for rondas in range(5):
    continuación = True
    while continuación:
        valorjugador1 = input("Elige piedra papel o tijeras:")
        valorjugador2 = input("Elige piedra papel o tijeras:")
        if valorjugador1 == valorjugador2:
            print("Hubo empate")
            empate = empate + 1
            continuación = False
        elif valorjugador1 == "piedra" and valorjugador2 == "papel":
            puntosjugador2 = puntosjugador2 + 1
            print("Ha ganado el jugador 2")
            continuación = False
        elif valorjugador1 == "piedra" and valorjugador2 == "tijeras":
            puntosjugador1 = puntosjugador1 + 1
            print("Ha ganado el jugador 1")
            continuación = False
        elif valorjugador1 == "papel" and valorjugador2 == "piedra":
            puntosjugador1 = puntosjugador1 + 1
            print("Ha ganado el jugador 1")
            continuación = False
        elif valorjugador1 == "papel" and valorjugador2 == "tijeras":
            puntosjugador2 = puntosjugador2 + 1
            print("Ha ganado el jugador 2")
            continuación = False
        elif valorjugador1 == "tijeras" and valorjugador2 == "piedra":
            puntosjugador2 = puntosjugador2 + 1
            print("Ha ganado el jugador 2")
            continuación = False
        elif valorjugador1 == "tijeras" and valorjugador2 == "papel":
            puntosjugador1 = puntosjugador1 + 1
            print("Ha ganado el jugador 1")
            continuación = False
        else:
            print("Por favor escriba bien")
            continuación = True
print("Han empatado",empate,"veces")
if puntosjugador1 > puntosjugador2:
    print("Ha ganado el jugador 1")
elif puntosjugador1 < puntosjugador2:
    print("Ha ganado el jugador 2")
else:
    print("Han empatado")
print("El jugador 1 ha ganado",puntosjugador1,"veces")
print("El jugador 2 ha ganado",puntosjugador2,"veces")

#otra manera de hacerlo
puntos_j1 = 0
puntos_j2 = 0
eleccion_jugador1 = ""
eleccion_jugador2 = ""
continuacion = True
for rondas in range(0,5):
    eleccion_jugador1 = input("Cuál eliges: piedra, papel o tijeras")
    eleccion_jugador1 = eleccion_jugador1.lower()
    while not (eleccion_jugador1 == "piedra" or eleccion_jugador1 == "papel" or eleccion_jugador1 == "tijeras"):
        print(eleccion_jugador1, "no es valida")
        eleccion_jugador1 = input("Cuál eliges: piedra, papel o tijeras")
    eleccion_jugador2 = input("Cuál eliges: piedra, papel o tijeras")
    eleccion_jugador2 = eleccion_jugador2.lower()
    while not (eleccion_jugador2 == "piedra" or eleccion_jugador2 == "papel" or eleccion_jugador2 == "tijeras"):
        print(eleccion_jugador2, "no es valida")
        eleccion_jugador2 = input("Cuál eliges: piedra, papel o tijeras")
    if eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijeras":
        print("Punto al jugador 1")
        puntos_j1 += 1
    elif eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra":
        print("Punto al jugador 1")
        puntos_j1 += 1
    elif eleccion_jugador1 == "tijeras" and eleccion_jugador2 == "papel":
        print("Punto al jugador 1")
        puntos_j1 += 1
    elif eleccion_jugador1 == eleccion_jugador2:
        print("Empate. Nadie suma puntos")
    else:
        print("Punto al jugador 2")
        puntos_j2 += 1
print("El jugador 1 tiene",puntos_j1,"puntos")
print("El jugador 2 tiene",puntos_j2,"puntos")
if puntos_j1 > puntos_j2:
    print("Gana el jugador 1")
elif puntos_j2 > puntos_j1:
     print("Gana el jugador 1")
else:
    print("Nadie gana .Empate")
    '''
# Usando listas mio
continuida2 = False
empate = 0
continuidad = True
puntos_j1 = 0
puntos_j2 = 0
respuesta_j1 = ""
respuesta_j2 = ""
opciones = ["piedra", "papel", "tijeras"]
for rondas in range(0,5):
    continuidad = True
    continuidad2 = True
    while continuidad:
        respuesta_j1 = input("Jugador 1 elige piedra papel o tijeras")
        while respuesta_j1 not in opciones:
            print("Por favor escriba bien")
            continuidad = True
            respuesta_j1 = input("Jugador 1 elige piedra papel o tijeras")
        respuesta_j2 = input("Jugador 2 elige piedra papel o tijeras")
        while respuesta_j2 not in opciones:
            print("Por favor escriba bien")
            continuidad = True
            respuesta_j2 = input("Jugador 2 elige piedra papel o tijeras")
        if respuesta_j1 == respuesta_j2:
            print("Hay un empate")
            empate += 1
        elif opciones.index(respuesta_j1) - opciones.index(respuesta_j2) == 1 or opciones.index(respuesta_j1) - opciones.index(respuesta_j2) == -2:
            print("Ha ganado el jugador 1")
            puntos_j1 += 1
            continuidad = False
        else:
            print("Ha ganado el jugador 2")
            puntos_j2 += 1
            continuidad = False
print("El jugador 1 tiene",puntos_j1,"puntos")
print("El jugador 2 tiene",puntos_j2,"puntos")
if puntos_j1 > puntos_j2:
    print("Gana el jugador 1")
elif puntos_j2 > puntos_j1:
    print("Gana el jugador 1")
else:
    print("Nadie gana .Empate")
