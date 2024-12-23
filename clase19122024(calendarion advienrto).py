# Escribe tu código aquí :-)
anterior=[]
correcto=True
while correcto:
    día=int(input("¿Qué día es el evento?:"))
    if día > 0 and día < 25:
        correcto=False
    else:
        print("Escriba el número del día")
        correcto=True
evento=str(input(f"Qué evento ocurre el día {día}:"))
with open("calendario","r+") as archivo:
    for i in range(1,día):
        anterior.append(archivo.read(i))
    archivo.seek(día+1)
    archivo.write(f"Día{día}:{evento}")
    anterior=str(anterior)
    archivo.seek(1)
    for i in range(0,len(anterior)):
        archivo.write(anterior[i])
