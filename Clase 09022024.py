# Escribe tu código aquí :-)
# Escribe tu código aquí :-)
MAXVER = int(input("Escribe como quieres que se de vertical"))
MAXHOR = int(input("Escribe como quieres que se en horizontal"))
nombre = str(input("Cuál es tu nombre"))
par = 0
calculo = 0
saludo = f"Hola,{nombre}"
tam_text = len(saludo)
espacios_total = MAXHOR - tam_text
espacios = espacios_total//2
text_espacio_izq = " "*espacios
text_espacio_der = " "*espacios
lineas = "-"*(MAXHOR-1)
medios = " "*(MAXHOR-1)
if MAXVER%2 == 0:
    calculo = MAXVER//2
    par = 1
else:
    calculo = MAXVER//2
print(calculo)
if espacios_total%2 == 0:
    text_espacio_der = " "*(espacios-1)
print(f" {lineas}")
if par == 1:
    for horizontal in range(0,(calculo-1)):
        print(f"|{medios}|")
    print(f"|{text_espacio_der}{saludo}{text_espacio_izq}|")
    for horizontal in range(0,calculo):
        print(f"|{medios}|")
    print(f" {lineas}")
else:
    for horizontal in range(0,calculo):
        print(f"|{medios}|")
    print(f"|{text_espacio_der}{saludo}{text_espacio_izq}|")
    for horizontal in range(0,calculo):
        print(f"|{medios}|")
    print(f" {lineas}")
