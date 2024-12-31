# Escribe tu código aquí :-)
continuar=True
with open("Mensaje2_entrelineas.txt","r") as adivinanzas:
    contenido=adivinanzas.readlines()
    for i in range(0,len(contenido)):
        linea=list(contenido[i])
        if linea[0] == "#" and continuar:
            print(linea[1])
            continuar=False
