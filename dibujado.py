import pygame

#Con los valores dados genera una linea de punto A a punto B
def linea(surface, color, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    error = dx - dy

    while x1 != x2 or y1 != y2:
        surface.set_at((x1, y1), color)
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x1 += sx
        if e2 < dx:
            error += dx
            y1 += sy
    pygame.display.flip()

#Con los valores de los 3 puntos dados manda a llamar a la función lineas y así generar el triangulo
def triangulo(surface, color, x1, y1, x2, y2, x3, y3):
    linea(surface, color, x1, y1, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x1, y1)

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
