# Escribe tu código aquí :-)
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
            elección1 = int(input("Escribe la coordenada jugador 1"))
            while not l[elección1] == " ":
                print("Escribe un valor valido")
                elección1 = int(input("Escribe la coordenada jugador 1"))
            l[elección1]=jugador1
            opcion = 2
        elif opcion == 2:
            elección2 = int(input("Escribe la coordenada jugador 2"))
            while not l[elección2] == " ":
                print("Escribe un valor valido")
                elección2 = int(input("Escribe la coordenada jugador 2"))
            l[elección2]=jugador2
            opcion = 1
            tabla = """
       |       |
   l[7]|l[8]   |l[9]
       |       |
  --------------------
       |       |
   l[4]|l[5]   |l[6]
       |       |
  --------------------
       |       |
   l[1]|l[2]   |l[3]
       |       |
"""
    return l
l = elecciones(jugador1,jugador2)
print(lista)
