# Escribe tu código aquí :-)
import pygame
import random

ANCHO = 500
ALTO = 500
TAM = (ANCHO, ALTO)
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Circulo"

pygame.display.set_caption(NOMBRE)
VENTANA = pygame.display.set_mode(TAM)

# el código de colores se puede encontrar en https://htmlcolorcodes.com/
# el RGB varía de 0 a 255

# x , y -> centro del circulo
x = 30
y = 30
ejecutar = True

while ejecutar:
    '''
    Cambiar el color del fondo a colores aleatorios
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    '''
    VENTANA.fill((25, 53, 86))

    # (PESTAÑA DONDE DIBUJAR, COLOR DEL CIRCULO EN RGB, (CORD. X, CORD. Y), RADIO DEL CIRCULO)
    for x in range(30,470):
        y = 30
        VENTANA.fill((25, 53, 86))
        pygame.draw.circle(VENTANA, (192, 37, 37), (x, y), 30)
        pygame.display.update()
    for y in range(30,470):
        x = 470
        VENTANA.fill((25, 53, 86))
        pygame.draw.circle(VENTANA, (192, 37, 37), (x, y), 30)
        pygame.display.update()
    for x in range(470,30,-1):
        y = 470
        VENTANA.fill((25, 53, 86))
        pygame.draw.circle(VENTANA, (192, 37, 37), (x, y), 30)
        pygame.display.update()
    for y in range(470,30,-1):
        x = 30
        VENTANA.fill((25, 53, 86))
        pygame.draw.circle(VENTANA, (192, 37, 37), (x, y), 30)
        pygame.display.update()


    pygame.display.update()
    # cerrar la ventana
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutar = False

pygame.quit()
