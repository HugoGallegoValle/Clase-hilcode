# Escribe tu código aquí :-)
while True:
    nombre = str(input("¿Cuál es tu nombre?:"))
    regalo= str(input("¿Que regalo quieres?:"))
    #print(lista)
    with open("lista de regalos","w") as carta:
        carta.write("Marco:Ordenador\n")
        carta.write("Sara:Árbol\n")
        carta.write("Alejnadro:Altavoz\n")
        carta.write(f"{nombre}:{regalo}")
    with open("lista de regalos","r") as carta:
        contenido=carta.readlines()
        print(contenido)
