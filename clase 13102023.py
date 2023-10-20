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
datos = []
Nombre = input("¿Cómo te llamas?")
Apellido = input("¿Cuáles son tus apellidos?")
Edad = int(input("¿Cuántos años tienes?"))
datos = [Nombre, Apellido, Edad,]
print("Te llamas :",datos[0])
print("Tus apellidos son:",datos[1])
print("Tu edad es de :",datos[2])
#comando.pop()
nombres = ["Ricardo", "Enrique", "Daniel", "Hugo", "Manuel"]
print(nombres)
nombres.pop(2)
print(nombres)
print("\n\n Con el remove")
#comando .remove()
nombres = ["Ricardo", "Enrique", "Daniel", "Hugo", "Manuel"]
print(nombres)
nombres.remove("Daniel")
print(nombres)
nombre = "Hugo"
nombres = ["Ricardo", "Enrique", "Daniel", "Hugo", "Manuel",nombres]
nombres.remove("Hugo")
#Actvidad pregntar y solo borrar apellidos
nombre = input("¿Cómo te llamas?")
apellidos= input("¿Cuál es tu apellido?")
edad= int(input("¿Cuántos años tienes?"))
datos = [nombre, apellidos, edad,]
datos.pop(1)
print("Te llamas:",datos[0])
print("Tienes:",datos[1],años)
print("Prueba de que se ha borrado",datos)

#tamaño de una lista
nombres = ["Ricardo", "Enrique", "Daniel", "Hugo", "Manuel"]
tam = len(nombres)
print("La lista tiene:",tam,"elementos")
