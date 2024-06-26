# Escribe tu código aquí :-)
import pygame
import random
ANCHO = 500
ALTO = 500
TAM = (ANCHO,ALTO)
CENTRO = (ANCHO/2,ALTO/2)
NOMBRE = "Círculo"
pygame.display.set_caption(NOMBRE)
VENTANA=pygame.display.set_mode(TAM)
VENTANA.fill((225,0,0))
pygame.display.update()
ejecutar = True
while ejecutar:
    '''
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    '''
    VENTANA.fill((225,0,0))
    #(donde dibujar(color),(coords.x y)(radio))
    pygame.draw.circle(VENTANA,(1,56,32),(123,20),20)
    pygame.display.update()
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutar=False
pygame.quit()
