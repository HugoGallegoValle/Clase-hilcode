# Escribe tu código aquí :-)
with open ("calendario","w") as archivo:
    for i in range(1,25):
        archivo.write(f"Dia{i}:\n")
        print(i)
