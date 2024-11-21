# Escribe tu código aquí :-)
import turtle
import random
continuar=True
respuesta = " "
num=0
sn= True
vn=0
verde = " "
país = " "
puntos = 0
verde=["portugal","irlanda","lituania","bielorrusia","bulgaria","italia","hungría","montenegro",
"moldavia","San Marinio","Chipre","Azerbaiyán"]
no_verde=["españa","andorra","francia","bélgica","países bajos","reino unido","alemania","dinamarca"
"polonia","letonia","estonia","finlandia","suecia","noruega","islandia","rusia","ucrania","rumanía",
"grecia","albania","macedonia del norte","serbia","Bosnia-Herzegovina","Croacia","Eslovenia","Ciudad del Vaticano"
,"Malta","Georgia","Armenia","Kazajistán"]
pantalla=turtle.Screen()
pantalla.bgcolor("blue")
tortuga=turtle.Turtle()
tortuga.shape("turtle")
tortuga.fillcolor("green")
tortuga.write("Observa la información del juego en la consola",align="center",font=("Arial","16"))
print("Para ganar el juego  tienes que mover la palanca")
print("Pero, ¿Cómo muevo la palanca?")
print("Para mover la palanca la palanca tiene que ser verde")
print("Para que se verde tienes que contestar las siguientes preguntas")
print("El sistema no reconcoe tildes")
def palanca_normal():
    tortuga.pendown()
    tortuga.goto(0,0)
    tortuga.forward(20)
    tortuga.right(90)
    tortuga.forward(3)
    tortuga.right(90)
    tortuga.forward(20)
    tortuga.right(90)
    tortuga.forward(3)
    tortuga.penup()
    tortuga.goto(0,100)
    print("Ya puedes ver la palanca en la pantalle que si lo consigues se levantará y se pondrá de color verde")
def palanca_ganada():
    tortuga.pendown()
    tortuga.right(90)
    tortuga.goto(0,0)
    tortuga.forward(20)
    tortuga.right(90)
    tortuga.forward(3)
    tortuga.right(90)
    tortuga.forward(20)
    tortuga.right(90)
    tortuga.forward(3)
    tortuga.penup()
    tortuga.goto(0,100)
def perdido():
    tortuga.clear()
    pantalla.bgcolor("Red")
    tortuga.write("Has perdido",align="center",font=("Arial","20"))
palanca_normal()
while continuar:
    for intentos in range(0,3):
        vn=random.randint(0,2)
        if vn == 0:
            num=random.randint(0,len(verde))
            país = verde[num]
            verde = "si"
        else:
            num=random.randint(0,len(no_verde))
            país = no_verde[num]
            verde = "no"
    print(f"Tiene {país} el color verde en su bandera")
    while sn:
        respuesta=input("Si o no:")
        respuesta = respuesta.lower()
        if respuesta == "si" or respuesta == "no":
            sn= False
        else:
            sn=True
    if respuesta == "si" and verde=="si":
        print("Correcto")
        puntos = puntos+1
        continuar=True
    elif respuesta == "no" and verde == "no":
        print("Correcto")
        puntos = puntos+1
        continuar=True
    else:
        print("Has perdido, ya no podrás levnatar la palanca verde")
        continuar=False
        perdido()
if puntos == 3:
    print("¡Has ganado¡")
    tortuga.clear()
    tortuga.begin_fill()
    tortuga.fillcolor("green")
    palanca_ganada()
    tortuga.end_fill
