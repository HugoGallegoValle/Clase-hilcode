# Escribe tu código aquí :-)
errores=0
with open("Mensaje4_reemplazos.txt","r+") as adivinanza:
    contenido = adivinanza.readlines()
    adivinanza.delete()
    for i in range(0,len(contenido)):
        if "ERROR" in contenido[i]:
            errores=errores+1
            contenido[i]=contenido[i].replace("ERROR","COSA")
            adivinanza.write(contenido[i])
    print(contenido)
    print(f"En el texto han sido reemplazados:{errores} errores")
