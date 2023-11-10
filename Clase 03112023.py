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
'''
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
