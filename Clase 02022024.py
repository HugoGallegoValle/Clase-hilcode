# Escribe tu código aquí :-)
# Escribe tu código aquí :-)
MAX = 30
nombre = str(input("Cuál es tu nombre"))
saludo = f"Hola,{nombre}"
tam_text = len(saludo)
espacios_total = MAX - tam_text
espacios = espacios_total//2
text_espacio_izq = " "*espacios
text_espacio_der = " "*espacios
if espacios_total%2 == 0:
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print(f"|{text_espacio_der}{saludo}{text_espacio_izq}|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
else:
    texto_espacio_der = " "*(espacios-1)
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print(f"|{text_espacio_der}{saludo}{text_espacio_izq}|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
