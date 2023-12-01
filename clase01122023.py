# Escribe tu código aquí :-)
'''
l_o = 0
nombre = "Hugo Gallego vollo petof"
nombre_lista = list(nombre)
for letra in nombre_lista:
    if letra == "o":
        l_o += 1
print("Tu nombre tiene ", l_o , "oes")
'''
#nombre con posición
posición_letras = 0
nombre = "Hugo Gallego"
nombre_lista = list(nombre)
for letras in range(0,len(nombre_lista)):
    posición_letras = nombre_lista[letras]
    if posición_letras == "o":
        print("Hay una o en la posición", letras)
