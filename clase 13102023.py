# Escribe tu código aquí :-)
'''
Bloque
de
comentarios
'''
print("Hola hoy es viernes")
nombre = input("¿Cuál es tu nombre?")
print("Te llamas"+nombre)
edad = int(input("¿Cuantos años tienes?"))
print("Tienes",edad,"años")
print("En diez años tendras ",edad +10)
#string --> str : Variables con letras, palabras y frases.
# integer --> int : Números enteros (sin parte decimal).
#lista --> list
apellidos = [] #lista vacía
edades = list() #otra lista vacía
nombres = ["Ricardo", "Enrique", "Daniel", "Hugo", "Manuel",]
print("apellidos:",apellidos)
print("nombres:",nombres)
print("El tipo de la variable nombre es:",type(nombres))
print("El primer nombre de la lista es:",nombres[0])
print("El sugundo nombre de la lista es:",nombres[1])
nombres.append("clovis")
print("Nombres:",nombres)
print("El sexto nombre de la lista es:",nombres[5])

#programa mio
Nombre = input("¿Cómo te llamas?")
Apellido = input("¿Cuáles son tus apellidos?")
Edad = input("¿Cuántos años tieenes?")
datos = [Nombre, Apellido, Edad,]
print("Te llamas :",datos[0])
print("Tus apellidos son:",datos[1])
print("Tu edad es de :",datos[2])
