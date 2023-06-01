#pylint: disable = E1101
#pylint: disable = C0103

import pygame
from dibujado import linea

#con los valores de spawneo y el tamaño de los lados calcula el contorno de un cuadrado
def cuadrado(surface, color, x, y, lado):
    x2 = x + lado
    y2 = y + lado

    linea(surface, color, x, y, x2, y)
    linea(surface, color, x2, y, x2, y2)
    linea(surface, color, x2, y2, x, y2)
    linea(surface, color, x, y2, x, y)

#Dados los valores centrales y el radio, genera un circulo perfecto
def circulo(surface, color, centro_x, centro_y, radio):
    x = 0
    y = radio
    d = 3 - 2 * radio

    while x<= y:
        surface.set_at((centro_x + x, centro_y + y), color)
        surface.set_at((centro_x - x, centro_y + y), color)
        surface.set_at((centro_x + x, centro_y - y), color)
        surface.set_at((centro_x - x, centro_y - y), color)
        surface.set_at((centro_x + y, centro_y + x), color)
        surface.set_at((centro_x - y, centro_y + x), color)
        surface.set_at((centro_x + y, centro_y - x), color)
        surface.set_at((centro_x - y, centro_y - x), color)

        x += 1
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -=1
    pygame.display.flip()
