# Escribe tu código aquí
points1 = 0
points2 = 0
posibilidades = ["piedra","papel","tijeras"]
continuación = True
for rondas in range(5):
    continuación = True
    while continuación:
        respuesta1 = input("Elige piedra papel o tijeras")
        respuesta2 = input("Elige piedra papel o tijeras")
        if respuesta1 == respuesta2:
            print("Hay un empate")
        elif respuesta1 == posibilidades[0] and respuesta2 == posibilidades[2]:
            print("Gana el jugador 1")
            points1 = points1 + 1
            continuación = False

