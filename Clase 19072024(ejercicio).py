# Escribe tu código aquí :-)
import pygame
ANCHO = 500
ALTO = 500
TAM = (ANCHO, ALTO)
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Circulo"
pygame.display.set_caption(NOMBRE)
VENTANA = pygame.display.set_mode(TAM)
#primero ventana, color y puntos(tupla)
#primero horizontal y despues vertical
pygame.draw.polygon(VENTANA, (145,53,82),((30,30),(80,30),(80,80),(30,80)))
pygame.display.update()
pygame.draw.polygon(VENTANA, (145,53,82),((150,30),(190,110),(110,110)))
pygame.display.update()
pygame.draw.polygon(VENTANA, (145,53,82),((200,30),(300,30),(300,80),(200,80)))
pygame.display.update()
pygame.draw.polygon(VENTANA, (145,53,82),((350,30),(430,30),(440,60),(340,60),(350,30)))
pygame.display.update()
pygame.draw.polygon(VENTANA, (145,53,82),((100,150),(132.5,300),(60.5,300)))
pygame.display.update()
pygame.draw.polygon(VENTANA, (145,53,82),((200,300),(250,300),(250,400),(300,400),(300,450),(450,450),(450,400),(400,400),(400,500)))
pygame.display.update()
