# Escribe tu código aquí :-)
import random

def aleatorio():
    jugador = random.randint(1,2)
    return jugador

def muestra_tabla(tabla):
    print('   |   |')
    print(' ' + tabla[7]  + ' | ' + tabla[8] + ' | ' + tabla[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tabla[4] + ' | ' + tabla[5] + ' | ' + tabla[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tabla[1] + ' | ' + tabla[2] + ' | ' + tabla[3])
    print('   |   |')

def elegir_X_O():
    jugador_1 = input("Jugador 1, ¿quieres X o O? ")
    jugador_1 = jugador_1.upper()
    # jugador_1 = jugador_1.lower()  para minusculas

    while not(jugador_1 == "X" or jugador_1 == "O"):
        print("¿Qué me estás contando?")
        jugador_1 = input("¿X o O? ")
        jugador_1 = jugador_1.upper()

    print("Vale :)")

    if jugador_1 == "X":
        jugador_2 = "O"
    else:
        jugador_2 = "X"

    return jugador_1, jugador_2

def cambio_posicion(tabla, jugador_1):
    posicion = int(input("¿Cuál posicion? "))
    while tabla[posicion] != " ":
        print("POSICIÓN OCUPADA")
        posicion = int(input("¿Cuál posicion? "))
    else:
        tabla[posicion] = jugador_1
def jug2(tabla,jugador_2):
    posicion = 0
    parar = 1
    if parar == 1:
        posicionul = random.randrange(1,9)
        posicion = posicionul
        parar = 0
    else:
        if posicionul > 7 or posicionful == 7:
            if posicionful == 9:
                posicion = posicionful-2
            else:
                posicion = posicionful -3
        else:
            posicion = posicionul+2
    while tabla[posicion] != " ":
        posicionul = random.randrange(1,9)
    else:
        tabla[posicion] = jugador_2
def victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2):
    ganador = 0

    if (tabla[1] == tabla[2] and tabla[2] == tabla[3]) and tabla[1] != ' ':
        ganador = tabla[1]
    elif (tabla[4] == tabla[5] and tabla[5] == tabla[6]) and tabla[5] != ' ':
        ganador = tabla[4]
    elif (tabla[7] == tabla[8] and tabla[8] == tabla[9]) and tabla[7] != ' ':
        ganador = tabla[7]
    elif (tabla[1] == tabla[4] and tabla[4] == tabla[7]) and tabla[1] != ' ':
        ganador = tabla[1]
    elif (tabla[2] == tabla[5] and tabla[5] == tabla[8]) and tabla[5] != ' ':
        ganador = tabla[2]
    elif (tabla[9] == tabla[6] and tabla[6] == tabla[3]) and tabla[9] != ' ':
        ganador = tabla[9]
    elif (tabla[1] == tabla[5] and tabla[5] == tabla[9]) and tabla[1] != ' ':
        ganador = tabla[1]
    elif (tabla[3] == tabla[5] and tabla[5] == tabla[7]) and tabla[3] != ' ':
        ganador = tabla[3]

    if ganador == jugador_1:
        print("Gana Jugador 1")
        puntos_j1 = puntos_j1 + 1
        print("--------------PUNTUACIÓN--------------")
        print("JUGADOR 1: ", puntos_j1, "PUNTOS")
        print("JUGADOR 2: ", puntos_j2, "PUNTOS")
        print("--------------------------------------")
    elif ganador == jugador_2:
        print("Gana Jugador 2")
        puntos_j2 = puntos_j2 + 1
        print("--------------PUNTUACIÓN--------------")
        print("JUGADOR 1: ", puntos_j1, "PUNTOS")
        print("JUGADOR 2: ", puntos_j2, "PUNTOS")
        print("--------------------------------------")
    elif " " not in tabla:
        print("Empate")
        print("--------------PUNTUACIÓN--------------")
        print("JUGADOR 1: ", puntos_j1, "PUNTOS")
        print("JUGADOR 2: ", puntos_j2, "PUNTOS")
        print("--------------------------------------")
        ganador = 1

    return ganador, puntos_j1, puntos_j2


if __name__ == "__main__":
    puntos_j1 = 0
    puntos_j2 = 0
    ganas_de_jugar = "SI"
    while ganas_de_jugar == "SI":

        tabla = ["#"," "," "," "," "," "," "," "," "," "]
        muestra_tabla(tabla)
        jugador_1, jugador_2 = elegir_X_O()
        jugador = aleatorio()
        ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)
        print(f"Empieza el jugador {jugador}.")

        while jugador == 1 and ganador == 0:
            print("Es el turno del jugador 1.")
            jugador1=cambio_posicion(tabla, jugador_1)
            muestra_tabla(tabla)
            ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)
            if ganador == 0:
                print("Es el turno del jugador 2.")
                jug2(tabla,jugador_2)
                muestra_tabla(tabla)
                ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)

        while jugador == 2 and ganador == 0:
            print("Es el turno del jugador 2.")
            jugador2=jug2(tabla,jugador_2)
            muestra_tabla(tabla)
            ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)
            if ganador == 0:
                print("Es el turno del jugador 1.")
                cambio_posicion(tabla, jugador_1)
                muestra_tabla(tabla)
                ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)

        ganas_de_jugar = input("¿Quieres jugar otra vez? SI o NO ")
        ganas_de_jugar = ganas_de_jugar.upper()
        while ganas_de_jugar != "SI" and ganas_de_jugar != "NO":
            ganas_de_jugar = input("¡RESPUESTA INVALIDA!\n¿Quieres jugar otra vez? SI o NO ")
            ganas_de_jugar = ganas_de_jugar.upper()
