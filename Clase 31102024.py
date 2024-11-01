# Escribe tu código aquí :-)
import turtle
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("red")
pantalla=turtle.Screen()
pantalla.title("Primer dibujo")
pantalla.bgcolor("blue")
for i in range(0,4):
    tortuga.forward(100)
    tortuga.right(90)

turtle.done()
