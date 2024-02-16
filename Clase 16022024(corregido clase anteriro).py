# Escribe tu código aquí :-)
# Definimos el tamaño de la caja
MAX_HORIZONTAL = 50
MAX_VERTICAL = 3

# El usuario escribe su nombre por teclado
nombre = input("¿Cuál es tu nombre? ")
saludo = f"Buenos días, {nombre}." # en la variable saludo, guardamos el texto que usaremos como saludo ya con el nombre añadido

# Ahora calculamos la cantidad de espacio en cada lado del saludo, aí podemos centralizar el texto
tam = len(saludo)
espacios = (MAX_HORIZONTAL-tam)
mitad = espacios//2

'''
Para centralizar el texto, guardamos en la variable 'mensaje' el saludo con espacios a la izquierda y a la derecha.
Los espacios a la derecha son definidos por "mitad+espacios%2" para que cuando el tamaño horizontal de la caja
sea un numero impar, se agregue de manera automática a la derecha del texto 1 espacio más para rellenar la caja.

Lo hacemos porque antes hemos divido de manera exacta espacios por 2 (espacios//2) y si es un número impar, al
hacer la división por 2, la división deja resto y esto cambia la apariencia de la caja al final de todo.
Haciendo esta suma para tener en cuenta ese resto la caja siempre tendrá la misma apariencia.

Es importante recordar que el operador "%" devuleve el resto de la division del número a su izquierda por
el número a su derecha. Por esto, al hacer espacios%2, si espacios es un valor impar, el resultado de la operación será 1,
y este 1 será sumado a la variable mitad en la derecha del saludo para que agregue más un espacio después del saludo.
Si espacios es par, la operación espacios%2 devuelve el valor 0, por lo que es lo mismo que no cambiar la cantidad
de espacios que será añadida a la derecha.
'''

mensaje = (' '*mitad) + saludo + (' '*(mitad+espacios%2))

linea_superior = " " + MAX_HORIZONTAL*"_" # establecemos como debe ser la parte superior de la caja (primera linea)
linea_inferior = "|" + MAX_HORIZONTAL*"_" + "|" # establecemos como debe ser la parte inferior de la caja (segunda linea)
linea_vacia = "|" + MAX_HORIZONTAL*" " + "|" # establecemos como debe ser las lineas de la caja que no tienen el saludo

# aqui de manera automatica creamos la caja con cuantas lineas hayamos establecido en la constante MAX_VERTICAL
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
