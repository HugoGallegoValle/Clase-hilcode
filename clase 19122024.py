# Escribe tu código aquí :-)
with open("Cartanavideña","w") as carta:
    carta.write("Queridos abuelos, espero que tengaís una feliz navidad y un buen inicio de 2025.\n")
    carta.write("Sois muy buenos abuelos y siempre me ayudáis\n")
    carta.write("por ejemplo, me habéis servido para probar la escritura y lectura de documentos en python\n")
    carta.write(" Sed felices, de vuestro nieto Hugo.\n")
with open("Cartanavideña","r") as carta:
    contenido=carta.read()
    print(contenido)
