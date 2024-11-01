# Escribe tu código aquí :-)
import turtle
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("red")
pantalla=turtle.Screen()
pantalla.title("Primer dibujo")
pantalla.bgcolor("blue")
tortuga.fillcolor("pink")
def hexagono():
    for i in range(0,6):
        tortuga.forward(30)
        tortuga.right(60)
def estrella():
    for i in range(0,6):
        tortuga.right(145)
        tortuga.forward(30)
tortuga.pensize(3)
tortuga.penup()
tortuga.goto(0,0)
tortuga.pendown()
hexagono()
tortuga.penup()
tortuga.goto(0,300)
tortuga.pendown()
estrella()
