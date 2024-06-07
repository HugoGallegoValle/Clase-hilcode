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

def cambio_posicion(tabla, jugador):
    posicion = int(input("¿Cuál posicion? "))
    while tabla[posicion] != " ":
        print("POSICIÓN OCUPADA")
        posicion = int(input("¿Cuál posicion? "))
    else:
        tabla[posicion] = jugador

def cambio_posicion_aleatorio(tabla, jugador):
    posicion = random.randrange(1,9)
    while tabla[posicion] != " ":
        posicion = random.randrange(1,9)
    else:
        print("El ordenador elige: ", posicion)
        tabla[posicion] = jugador

def busqueda(tabla, jugador_1):
    jugadas_p1 = []
    for i in range(len(tabla)):
        if tabla[i] == jugador_1:
            jugadas_p1.append(i)
    return jugadas_p1

def cercanas(tabla, jugador_1, jugadas_p1):
    #HORIZONTALES
    #primera fila
    mapa = []
    for i in jugadas_p1:
        if i < 3:
            if tabla[i + 1] == " ":
                mapa.append(i + 1)
        if i > 1 and i < 4:
            if tabla[i - 1] == " ":
                mapa.append(i - 1)
    #segunda fila
        if i < 6 and i > 3:
            if tabla[i + 1] == " ":
                mapa.append(i + 1)
        if i > 4 and i < 7:
            if tabla[i - 1] == " ":
                mapa.append(i - 1)
    #tercera fila
        if i < 9 and i > 6:
            if tabla[i + 1] == " ":
                mapa.append(i + 1)
        if i > 7:
            if tabla[i - 1] == " ":
                mapa.append(i - 1)
    #VERTICAL
    #primera fila
        if i < 7:
            if tabla[i + 3] == " ":
                mapa.append(i + 1)
        if i > 1 and i <= 4:
            if tabla[i - 3] == " ":
                mapa.append(i - 1)
    #segunda fila
        if i < 8 and i > 2:
            if tabla[i + 3] == " ":
                mapa.append(i + 1)
        if i > 2 and i <= 5:
            if tabla[i - 3] == " ":
                mapa.append(i - 1)
    #tercera fila
        if i < 9 and i > 3:
            if tabla[i + 3] == " ":
                mapa.append(i + 1)
        if i >= 6:
            if tabla[i - 3] == " ":
                mapa.append(i - 1)
    #DIAGONAL
    #primera fila
        if i == 5 or i == 1:
            if [i + 4] == " ":
                mapa.append(i + 4)
        if i == 9 or i == 5 :
            if tabla[i - 4] == " ":
                mapa.append(i - 4)
    #segunda diagonal
        if i == 5 or i == 3:
            if tabla[i + 4] == " ":
                mapa.append(i + 2)
        if i == 5 or i == 5 or i == 7:
            if tabla[i - 4] == " ":
                mapa.append(i - 2)
        return mapa
#cercanas jugador
    for i in jugadas_p1:
        if i < 4:
            if tabla[i + 1] == jugador_1:
                if tabla[i+2] == " ":
                    mapa.append(i + 1)
        if i > 1 and i < 4:
            if tabla[i - 1] == jugador_1:
                if tabla[i-2] == " ":
                    mapa.append(i - 1)
    #segunda fila
        if i < 6 and i > 3:
            if tabla[i + 1] == jugador_1:
                if tabla[i+2] == " ":
                    mapa.append(i + 1)
        if i > 4 and i < 7:
            if tabla[i - 1] == jugador_1:
                if tabla[i-2] == " ":
                    mapa.append(i - 1)
    #tercera fila
        if i < 9 and i > 6:
            if tabla[i + 1] == jugador_1:
                if tabla[i-2] == " ":
                    mapa.append(i - 1)
        if i > 7:
            if tabla[i - 1] == jugador_1:

                mapa.append(i - 1)
    #VERTICAL
    #primera fila
        if i < 7:
            if tabla[i + 3] == jugador_1:

                mapa.append(i + 1)
        if i > 1 and i <= 4:
            if tabla[i - 3] == jugador_1:

                mapa.append(i - 1)
    #segunda fila
        if i < 8 and i > 2:
            if tabla[i + 3] == jugador_1:
                mapa=[]
                mapa.append(i + 1)
        if i > 2 and i <= 5:
            if tabla[i - 3] == jugador_1:

                mapa.append(i - 1)
    #tercera fila
        if i < 9 and i > 3:
            if tabla[i + 3] == jugador_1:

                mapa.append(i + 1)
        if i >= 6:
            if tabla[i - 3] == jugador_1:

                mapa.append(i - 1)
    #DIAGONAL
    #primera fila
        if i == 5 or i == 1:
            if tabla[i + 4] == jugador_1:

                mapa.append(i + 4)
        if i == 9 or i == 5 :
            if tabla[i - 4] == jugador_1:

                mapa.append(i - 4)
    #segunda diagonal
        if i == 5 or i == 3:
            if tabla[i + 4] == jugador_1:

                mapa.append(i + 2)
        if jugadas_p1[i] == 5 or jugadas_p1 == 5 or jugadas_p1 == 7:
            if tabla[jugadas_p1[i] - 4] == jugador_1:

                mapa.append(jugadas_p1[i] - 2)
    #MIRAR VALORES CONSECUTIVOS
        if i < 4 and tabla[i+3] == jugador_1 and tabla[i+6] == " ":
            mapa = [i+6]
            return mapa
        if i > 3:
            if tabla[i-3] == " ":
                mapa.append(i-3)
    #MIRAR VALORES CONSECUTIVOS EN DIAGONAL1
        if i < 9 and tabla[i+4] == jugador_1 and tabla[i+8] == " ":
            mapa = [i+8]
            return mapa
        if i > 1:
            if tabla[i-4] == " ":
                mapa.append(i-4)
    ############################♣
        if i < 1 and tabla[i-4] == jugador_1 and tabla[i-8] == " ":
            mapa = [i-8]
            return mapa
        if i > 9:
            if tabla[i+4] == " ":
                mapa.append(i+4)
    #MIRAR VALORES CONSECUTIVOS EN DIAGONAL2
        if i < 7 and tabla[i+4] == jugador_1 and tabla[i+8] == " ":
            mapa=[i+8]
            return mapa
        if i > 3:
            if tabla[i-4] == " ":
                mapa.append(i-4)
    ############################
        if i < 3 and tabla[i-4] == jugador_1 and tabla[i-8] == " ":
            mapa = [i-8]
            return mapa
        if i > 7:
            if tabla[i+4] == " ":
                mapa.append(i+4)
    return mapa
def colocar(mapa):
    repetido = 0
    grande = 0
    aviso = 0
    máximo = 0
    grandes = []
    for i in range(0,len(mapa)):
        if mapa[i] in grandes:
            repetido = mapa[i]
            aviso = 0
            for i in range(0,len(mapa)):
                if mapa[i] == repetido:
                    aviso = aviso + 1
        grandes.append(mapa[i])
        if aviso > máximo:
            máximo = aviso
            max_num = repetido
            jugada = max_num


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
            cambio_posicion(tabla, jugador_1)
            muestra_tabla(tabla)
            ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)
            if ganador == 0:
                print("Es el turno del jugador 2.")
                cambio_posicion_aleatorio(tabla, jugador_2)
                muestra_tabla(tabla)
                ganador, puntos_j1, puntos_j2 = victoria(tabla, jugador_1, jugador_2, puntos_j1, puntos_j2)

        while jugador == 2 and ganador == 0:
            print("Es el turno del jugador 2.")
            cambio_posicion_aleatorio(tabla, jugador_2)
            muestra_tabla(tabla)
            jugadas_p1=busqueda(tabla,jugador_1)
            mapa=cercanas(tabla,jugador_1,jugadas_p1)
            juagada=colocar(mapa)
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