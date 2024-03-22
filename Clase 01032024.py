# Escribe tu código aquí :-)
total = True
empate = 0
puntos1 = 0
puntos2 = 0
def gana(l):
    continuación = True
    ganador = " "
    if (l[3] == l[2] and l[2] == l[1]) and not(l[3] == " "):
        continuación = False
        ganador = l[1]
    elif (l[4] == l[5] and l[5] == l[6]) and (not l[4] == " "):
        continuación = False
        ganador = l[4]
    elif (l[7] == l[8] and l[8] == l[9]) and (not l[7] == " "):
        continuación = False
        ganador = l[9]
    elif (l[3] == l[6] and l[6] == l[9]) and (not l[3] == " "):
        continuación = False
        ganador = l[9]
    elif (l[2] == l[5] and l[5] == l[8]) and (not l[2] == " "):
        continuación = False
        ganador = l[8]
    elif (l[1] == l[4] and l[4] == l[7]) and (not l[1] == " "):
        continuación = False
        ganador = l[7]
    elif (l[3] == l[5] and l[5] == l[7]) and (not l[3] == " "):
        continuación = False
        ganador = l[7]
    elif (l[1] == l[5] and l[5] == l[9]) and (not l[1] == " "):
        continuación = False
        ganador = l[9]
    elif " " not in l:
        continuación = "Empate"
        ganador = "Empate"
    return continuación,ganador
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

while total:


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
        while continuación and continuación != "Empate":
            if (opcion == 1 and continuación) and continuación != "Empate":
                elección1 = int(input("Escribe la coordenada jugador 1:"))
                while not (type(elección1) == int) or elección1 > 9 or elección1 < 1 or (l[elección1] != " "):
                    print("Escribe un valor valido")
                    elección1 = int(input("Escribe la coordenada jugador 1:"))
                l[elección1]=jugador1
                opcion = 2
                continuación, ganador=gana(l)
            elif (opcion == 2 and continuación)and continuación != "Empate":
                elección2 = int(input("Escribe la coordenada jugador 2:"))
                while not (type(elección2) == int) or elección2 > 9 or elección2 < 1 or (l[elección2] != " "):
                    print("Escribe un valor valido")
                    elección2 = int(input("Escribe la coordenada jugador 2:"))
                l[elección2]=jugador2
                opcion = 1
                continuación,ganador=gana(l)
            dibuja_tabla(l)
        return l,ganador,continuación
    l,ganador,continuación=elecciones(jugador1,jugador2)
    if ganador != "Empate":
        print("El ganador es:",ganador)
        if ganador == jugador1:
            puntos1 = puntos1 + 1
        else:
            puntos2 = puntos2 + 1
    else:
        print("Hay un empate")
        empate = empate + 1
    pregunta = str(input("¿Deseas volver a jugar?"))
    pregunta = pregunta.lower()
    while not pregunta == "sí" and pregunta == "no":
        pregunta = str(input("¿Deseas volver a jugar?"))
        pregunta = pregunta.lower()
    if pregunta == "si" or pregunta == "sí":
        total = True
    else:
        total = False
print ("Jugador 1 ha ganado:",puntos1)
print("Jugador 2 ha ganado:",puntos2)
print("Hubo",empate,"empates")
