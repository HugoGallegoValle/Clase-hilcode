# Escribe tu código aquí :-)
continuar=True
with open("Mensaje2_entrelineas.txt","r") as adivinanzas:
    contenido=adivinanzas.readlines()
    for linea in range(0,len(contenido)):
        letra=list(contenido[linea])
        if letra[0] == "#" and continuar:
            print(contenido[linea])
            continuar=False

