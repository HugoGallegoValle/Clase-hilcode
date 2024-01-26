# Escribe tu código aquí :-)
'''
calculo_resto = 0
calculo = 0
variable = 0
print(" -----------------------------")
print("|                              |")
print("|                              |")
print("|                              |")
print("|                              |")
print("|                              |")
print(" -----------------------------")
nombre = str(input("¿Cómo te llamas?"))
print(" -----------------------------")
print("|                              |")
print("|                              |")
print("|       Hola",nombre,"             |")
print("|                              |")
print("|                              |")
print(" -----------------------------")
'''
#autoático centralizado
espacios = " "
espaciosrest = " "
resto = 0
calculo = 0
nombre = input("¿Cómo te llamas?")
calculo = 0
resto = (30-len(nombre)-4)%2
if calculo == 0:
    calculo = (30-len(nombre)-4)/2
        espacios = " " * calculo
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print("|",espacios"Hola",nombreespacios"|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
else:
    calculo = (30-len(nombre)-4)/2
    espaciosrest = claculo * " "
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print("|",espaciosrest,espacios,"Hola",nombre,espacios,"|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
