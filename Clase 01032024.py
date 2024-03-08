# Escribe tu código aquí :-)
def dibuja_tabla():
    tabla = """
     |       |
     |       |
     |       |
--------------------
     |       |
     |       |
     |       |
--------------------
     |       |
     |       |
     |       |
"""
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

tabla = dibuja_tabla()
print(tabla)
opcion = 1
jugador1, jugador2 = pregunta()
def elecciones(jugador1,jugador2):
    l = ["@"," "," "," "," "," "," "," "," "," "]
    opcion = 1
    while " " in l:
        if opcion == 1:
            elección1 = int(input("Escribe la coordenada jugador 1:"))
            while not (type(elección1) == int) or elección1 > 9 or elección1 < 1 or (l[elección1] != " "):
                print("Escribe un valor valido")
                elección1 = int(input("Escribe la coordenada jugador 1:"))
            l[elección1]=jugador1
            opcion = 2
        elif opcion == 2:
            elección2 = int(input("Escribe la coordenada jugador 2:"))
            while not (type(elección2) == int) or elección2 > 9 or elección2 < 1 or (l[elección2] != " "):
                print("Escribe un valor valido")
                elección2 = int(input("Escribe la coordenada jugador 2:"))
            l[elección2]=jugador2
            opcion = 1
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
elecciones(jugador1,jugador2)
