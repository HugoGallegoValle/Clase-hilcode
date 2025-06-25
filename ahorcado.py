# Escribe tu código aquí :-)
import turtle
palabra = "calendario"
fallos=0
pos=0
cinco=-15
continuar=0
no_esta=[]
posiciones=[]
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("black")
pantalla = turtle.Screen()
pantalla.title("Ahorcado")
pantalla.bgcolor("white")
tortuga.goto(0,0)
for i in range(0,len(palabra)):
    tortuga.goto(pos, 0)
    tortuga.pendown()
    pos=pos+10
    tortuga.goto(pos,0)
    tortuga.penup()
    pos=pos+10
    cinco=cinco+20
    posiciones.append(cinco)
    print(posiciones)
while not continuar==len(palabra):
    letra=input("Escribe una letra:")
    if letra in palabra:
        for i in range(0,len(palabra)):
            if palabra[i] == letra:
                posicion=i
                letra_s=palabra[posicion]
                tortuga.goto(posiciones[posicion],0)
                tortuga.write(letra_s, font=("Arial", 15, "normal"))
                tortuga.goto(200,100)
                continuar=continuar+1
    else:
        print(f"Lo sentimos paro la letra {letra} no esta en la palabra")
        no_esta.append(letra)
        print(f"Las siguientes letras no están{no_esta}")
        fallos=fallos+1
        if fallos==1:
            tortuga.penup()
            tortuga.goto(-250,0)
            tortuga.pendown()
            tortuga.goto(-250,150)
        if fallos==2:
            tortuga.penup()
            tortuga.goto(-250,150)
            tortuga.pendown()
            tortuga.goto(-215,150)
        if fallos==3:
            tortuga.penup()
            tortuga.goto(-215,150)
            tortuga.pendown()
            tortuga.goto(-215,115)
        if fallos==4:
            tortuga.penup()
            tortuga.goto(-215,75)
            tortuga.pendown()
            tortuga.circle(20)
        if fallos==5:
            tortuga.penup()
            tortuga.goto(-215,75)
            tortuga.pendown()
            tortuga.goto(-215,0)
        if fallos == 6:
            tortuga.penup()
            tortuga.goto(-216,50)
            tortuga.pendown()
            tortuga.goto(-246,50)
            tortuga.penup()
            tortuga.goto(-214,50)
            tortuga.pendown()
            tortuga.goto(-184,50)
        if fallos==7:
            break
        tortuga.penup()
if continuar==len(palabra):
    pantalla.clear()
    tortuga.color("green")
    tortuga.write("Has ganado", align="center", font=("Arial", 30, "normal"))
else:
    pantalla.clear()
    tortuga.color("red")
    tortuga.write("Has perdido", align="center", font=("Arial", 30, "normal"))
turtle.done()
