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
    lista = ["@"," "," "," "," "," "," "," "," "," "," "]
    opcion = 1
    while " " in lista:
        if opcion == 1:
            elección1 = int(input("Escribe la coordenada jugador 1"))
            lista[elección1]=jugador1
            opcion = 2
        if opcion == 2:
            elección2 = int(input("Escribe la coordenada jugador 2"))
            lista[elección2]=jugador2
            opcion = 1
    return lista
lista = elecciones(jugador1,jugador2)
print(lista)
