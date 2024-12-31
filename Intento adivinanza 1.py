# Escribe tu código aquí :-)
with open("Mensaje1_adivinanza.txt","r") as adivinanza:
    contenido=adivinanza.readlines()
    print(contenido)
    usuario=input("¿Cuál es la respuesta?:")
    print(f"La primera letra de la contraseña es:{usuario[0]}")
