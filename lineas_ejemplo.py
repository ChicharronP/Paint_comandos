import pygame
import sys

def generar_linea_pygame(a, b, c, d):
    """
    Genera la ecuación de una línea en función de cuatro valores dados y la dibuja en una ventana utilizando Pygame.
    
    Argumentos:
    a, b, c, d -- Los cuatro valores para generar la línea.
    
    Retorna:
    None
    """
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dibujar línea")

    # Construir la ecuación de la línea
    m = (d - b) / (c - a)
    b = b - m * a

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0, 0, 0), (0, int(b)), (width, int(m * width + b)), 2)

        pygame.display.flip()

    pygame.quit()


# Ejemplo de uso
a = 0
b = 300
c = 800
d = 300

generar_linea_pygame(a, b, c, d)
