# Escribe tu código aquí :-)
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
#autoático centralizado
calculo_resto = len(nombre)%25
if calculo_resto == 0:
    calculo = len(nombre)/25
    print("|")
    for espacios in range(0,calculo):
        print(" ")
    print("Holas",nombre)
    for espacios in range(0,calculo):
        print(" ")
    print("|")
