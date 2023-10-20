# Escribe tu código aquí :-)
dinero = float(input("Cuánto dienro tienes"))
chuche = 1
pastel = 3.5
pan = 0.85
nocilla = 3.5
compra = chuche + pastel + pan + nocilla
print("El total de la compra es de",compra,"€")
if dinero >= compra:
    print("Compra aceptada.\n Tienes ahora",dinero-compra,"€")
else:
    print("Trajeta denegada")
    print("Te faltan:", compra - dinero,"€")
#mi programa
masclassnum = 16
usarameclassnum =  int(input("¿Cuántos alumnos y alumnas hay en tu clase?"))
if masclassnum >= usarameclassnum:
    print("Tu clase tiene un número correcto de alumnos/as")
else:
    print("Tu clase es demasiado grande")
    print("necesitas",usarameclassnum - masclassnum,"alumnos/as menos")
