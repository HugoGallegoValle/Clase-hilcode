# Escribe tu código aquí :-)
def preguntas ():
    MAX_HORIZONTAL = int(input("¿Cómo quieres que tenga de horizontal?"))
    MAX_VERTICAL = int(input("¿Cómo quieres que tenga de vertical?"))
    return MAX_HORIZONTAL, MAX_VERTICAL
MAX_HORIZONTAL, MAX_VERTICAL = preguntas()
def saludo ():
    nombre = input("¿Cuál es tu nombre? ")
    saludo = f"Buenos días, {nombre}."
    return nombre, saludo
nombre, saludo = saludo()
def dibujar_caja (saludo, MAX_HORIZONTAL, MAX_VERTICAL):
    tam = len(saludo)
    espacios = (MAX_HORIZONTAL-tam)
    mitad = espacios//2
    mensaje = (' '*mitad) + saludo + (' '*(mitad+espacios%2))
    linea_superior = " " + MAX_HORIZONTAL*"_"
    linea_inferior = "|" + MAX_HORIZONTAL*"_" + "|"
    linea_vacia = "|" + MAX_HORIZONTAL*" " + "|"
    for i in range(-1,MAX_VERTICAL):
        if i == -1:
            print(f"{linea_superior}")

        elif i+1 == MAX_VERTICAL//2 and MAX_VERTICAL%2==0:
            print(f"|{mensaje}|")

        elif i == MAX_VERTICAL//2 and MAX_VERTICAL%2==1:
            print(f"|{mensaje}|")

        elif i == MAX_VERTICAL-1:
            print(f"{linea_inferior}")

        else:
            print(f"{linea_vacia}")
dibujar_caja(saludo, MAX_HORIZONTAL, MAX_VERTICAL)
