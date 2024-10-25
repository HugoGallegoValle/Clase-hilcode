# Escribe tu código aquí :-)
'''números=[]
números_pares[] #PARA CREAR UNA LISTA NECESITO PONER EL IGUAL ANTES DEL CORCHETE
for i in range (1,101):
    números.append(i)
for i in range(1,101): #EL ELEMENTO 101 ESTÁ FUERA DE RANGO, EN LA LISTA QUE HAS CREADO, LOS INDICES VAN DEL 0 AL 100
    if números[i]%2 == 0:
        números_pares.append(números[i])
print(f"Todos los números{números}")
print(f"Números pares{números_pares}")'''

nUmeros=[]
nUmeros_pares=[]
for i in range (1,101):
    nUmeros.append(i)
for i in range(1,100):
    if nUmeros[i]%2 == 0:
        nUmeros_pares.append(nUmeros[i])
print("Todos los números", nUmeros)
print("\nNúmeros pares",nUmeros_pares)
