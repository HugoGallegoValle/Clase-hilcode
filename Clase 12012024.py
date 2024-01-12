# Escribe tu código aquí :-)
continuidad = True
continuidad2 = True
borrador = 0
calculo = ""
selección = ""
secret = int(input("Escribe un numero del 1 al 100 para que la computadora lo adivine"))
números = []
for i in range(0,100):
    números.append(i)
while continuidad:
    calculo = len(números)//2
    calculo = int(calculo)
    borrador = int(borrador)
    selección = números[calculo]
    selección = int(selección)
    if secret == selección:
        continuidad = False
        print("Lo onseguiste")
    elif selección < secret:
        while continuidad2:
            borrador = borrador + 1
            if borrador < selección:
                números.pop(borrador)
            else:
                continuidad2 = False
    elif selección > secret:
        while continuidad2:
            borrador = borrador + 1
            if borrador > selección:
                números.pop(borrador)
            else:
                continuidad2 = False
