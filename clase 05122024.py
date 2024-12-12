# Escribe tu código aquí :-)
import turtle
pantalla=turtle.Screen()
pantalla.title("Pong")
pantalla.bgcolor("black")
pantalla.setup(width=800,height=600)

palaizq= turtle.Turtle()
palaizq.speed(0)
palaizq.color("white")
palaizq.shape("square")
palaizq.penup()
palaizq.goto(-375,0)
palaizq.shapesize(stretch_wid=6,stretch_len=1)

palader=turtle.Turtle()
palader.speed(0)
palader.color("white")
palader.shape("square")
palader.penup()
palader.goto(375,0)
palader.shapesize(stretch_wid=6,stretch_len=1)

y= palaizq.ycor()
palaizq.sety(y+137)
y = palaizq.ycor()
'''
texto=turtle.Turtle()
texto.color("white")
texto.write(y)
'''
y1= palader.ycor()
palader.sety(y1-37)
y1 = palaizq.ycor()
'''
texto1=turtle.Turtle()
texto1.color("white")
texto1.write(y1)

'''
def a():
    y = palaizq.ycor()
    if y < 250:
        palaizq.sety(y+20)
def b():
    y = palaizq.ycor()
    if y > -250:
        palaizq.sety(y-20)
def c():
    y = palader.ycor()
    if y < 250:
        palader.sety(y+20)
def d():
    y = palader.ycor()
    if y > -250:
        palader.sety(y-20)
pantalla.listen()
pantalla.onkeypress(a,"w")
pantalla.onkeypress(b,"s")
pantalla.onkeypress(c,"e")
pantalla.onkeypress(d,"o")

pelota=turtle.Turtle()
pelota.shape("circle")
pelota.color("white")
pelota.goto(0,0)
pelota.dx=2.5
pelota.dy=2.5
marcador_izq=0
marcador_der=0
marcador=turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write(f"Jugador Izq :{marcador_izq} Jugador Der: {marcador_der}",align="center",font=("Courier",24,"normal"))
while True:
    pelota.penup()
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *=-1
    if (pelota.xcor() > 365 and pelota.xcor() < 375) and (pelota.ycor() < palader.ycor() + 50 and pelota.ycor() > palader.ycor()-50):
        pelota.setx(340)
        pelota.dx *= -1
    if (pelota.xcor() < -365 and pelota.xcor() > -375) and (pelota.ycor() < palaizq.ycor() + 50 and pelota.ycor() > palaizq.ycor()-50):
        pelota.setx(-340)
        pelota.dx *= -1
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *=-1
        marcador_izq=marcador_izq+1
        marcador.clear()
        marcador.write(f"Jugador Izq :{marcador_izq} Jugador Der: {marcador_der}",align="center",font=("Courier",24,"normal"))
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *=-1
        marcador_der=marcador_der+1
        marcador.clear()
        marcador.write(f"Jugador Izq :{marcador_izq} Jugador Der: {marcador_der}",align="center",font=("Courier",24,"normal"))
