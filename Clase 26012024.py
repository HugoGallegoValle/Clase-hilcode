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
resto = (30-len(nombre)-4)%2
if calculo == 0:
    calculo = (30-len(nombre)-4)/2
    espacios = " " * calculo
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print("|",espacios,"Hola",nombre,espacios,"|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
else:
    calculo = (30-len(nombre)-4)/2
    espaciosrest = resto * " "
    espacios = calculo * " "
    print(" -----------------------------")
    print("|                              |")
    print("|                              |")
    print("|",espaciosrest,espacios,"Hola",nombre,espacios,"|")
    print("|                              |")
    print("|                              |")
    print(" -----------------------------")
