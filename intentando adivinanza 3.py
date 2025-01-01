# Escribe tu código aquí :-)
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","s","T","U","V","W","X","Y","Z"]
alfabeto_rot13 = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"]
letra= []
posicion=0
traduccion=[]
with open("Mensaje3_ROT13.txt","r") as adivinanza:
    contenido=adivinanza.readlines()
    for i in range(0,len(contenido)):
        letra.append(list(contenido[i].upper()))
    print(letra)
    for i in range(0,len(letra)):
        if letra[i] not in alfabeto_rot13:
            traduccion.append(letra[i])
        posicion=alfabeto_rot13.index(letra[i])
        traduccion.append(alfabeto[posicion])
    print(traduccion)

