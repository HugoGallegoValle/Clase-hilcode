# Escribe tu código aquí :-)
# Escribe tu código aquí :-)
MAX = int(input("¿Cómo de grande quieres que sea tu caja?"))
nombre = str(input("Cuál es tu nombre"))
saludo = f"Hola,{nombre}"
tam_text = len(saludo)
espacios_total = MAX - tam_text
espacios = espacios_total//2
text_espacio_izq = " "*espacios
text_espacio_der = " "*espacios
lineas = "-"*(MAX-1)
medios = " "*(MAX-1)
if espacios_total%2 == 0:
    texto_espacio_der = " "*(espacios-1)
print(f" {lineas}")
print(f"{medios}|")
print(f"|{medios}|")
print(f"|{text_espacio_der}{saludo}{text_espacio_izq}|")
print(f"|{medios}|")
print(f"|{medios}|")
print(f" {lineas}")
