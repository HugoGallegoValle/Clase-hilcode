# Escribe tu código aquí :-)
def ganador(l):
    continuación = True
    if (l[3] == l[2] and l[2] == l[1]) and not(l[3] == " "):
        continuación = False
        print("El ganador/a es:",l[1])
    elif (l[4] == l[5] and l[5] == l[6]) and (not l[4] == " "):
        continuación = False
        print("El ganador/a es:",l[4])
    elif (l[7] == l[8] and l[8] == l[9]) and (not l[7] == " "):
        continuación = False
        print("El ganador/a es:",l[9])
    elif (l[3] == l[6] and l[6] == l[9]) and (not l[3] == " "):
        continuación = False
        print("El ganador/a es:",l[9])
    elif (l[2] == l[5] and l[5] == l[8]) and (not l[2] == " "):
        continuación = False
        print("El ganador/a es:",l[8])
    elif (l[1] == l[4] and l[4] == l[7]) and (not l[1] == " "):
        continuación = False
        print("El ganador/a es:",l[7])
    elif (l[3] == l[5] and l[5] == l[7]) and (not l[3] == " "):
        continuación = False
        print("El ganador/a es:",l[7])
    elif (l[1] == l[5] and l[5] == l[9]) and (not l[1] == " "):
        continuación = False
        print("El ganador/a es:",l[9])
    return continuación
def dibuja_tabla(l):
    tabla = f"""
          |       |
      {l[9]}   |   {l[8]}   |   {l[7]}
          |       |
     --------------------
          |       |
      {l[6]}   |   {l[5]}   |   {l[4]}
          |       |
      --------------------
          |       |
      {l[3]}   |   {l[2]}   |   {l[1]}

          |       |

    """
    print(tabla)
    return tabla

def pregunta():
    opciones = ("X", "O")
    jugador1 = input("¿Que eliges, la 'X' o la 'O'? ")
    jugador1 = jugador1.upper()
    while jugador1 not in opciones:
        print("INVALIDO.")
        print("¿'X' o 'O'?")
        jugador1 = input("¿Que eliges, la 'X' o la 'O'? ")
        jugador1 = jugador1.upper()

    if jugador1 == opciones[0]:
        jugador2 = opciones[1]
    else:
        jugador2 = opciones[0]

    return jugador1, jugador2
opcion = 1
jugador1, jugador2 = pregunta()
def elecciones(jugador1,jugador2):
    l = ["@"," "," "," "," "," "," "," "," "," "]
    tabla = dibuja_tabla(l)
    opcion = 1
    continuación = True
    while " " in l or continuación:
        if opcion == 1 and continuación:
            elección1 = int(input("Escribe la coordenada jugador 1:"))
            while not (type(elección1) == int) or elección1 > 9 or elección1 < 1 or (l[elección1] != " "):
                print("Escribe un valor valido")
                elección1 = int(input("Escribe la coordenada jugador 1:"))
            l[elección1]=jugador1
            opcion = 2
            continuación=ganador(l)
        elif opcion == 2 and continuación:
            elección2 = int(input("Escribe la coordenada jugador 2:"))
            while not (type(elección2) == int) or elección2 > 9 or elección2 < 1 or (l[elección2] != " "):
                print("Escribe un valor valido")
                elección2 = int(input("Escribe la coordenada jugador 2:"))
            l[elección2]=jugador2
            opcion = 1
            continuación=ganador(l)
        dibuja_tabla(l)
    return l
elecciones(jugador1,jugador2)
