import pygame

def linea_h(surface, color, x1, x2, y, thickness):
    for t in range(thickness):
        y_offset = y + t  # Aumentar el desplazamiento vertical en cada iteración
        for i in range(x1, x2 + 1):
            surface.set_at((i, y_offset), color)
    pygame.display.flip()

def linea_v(surface, color, x, y1, y2, thickness):
    for t in range(thickness):
        x_offset = x + t  # Aumentar el desplazamiento horizontal en cada iteración
        for i in range(y1, y2 + 1):
            surface.set_at((x_offset, i), color)
    pygame.display.flip()

def linea_d(surface, color, x1, y1, x2, y2, thickness):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    error = dx - dy

    for t in range(thickness):
        x_offset = x1 + t * sx  # Aumentar el desplazamiento horizontal en cada iteración
        y_offset = y1 + t * sy  # Aumentar el desplazamiento vertical en cada iteración

        while x_offset != x2 or y_offset != y2:
            surface.set_at((x_offset, y_offset), color)
            e2 = 2 * error
            if e2 > -dy:
                error -= dy
                x_offset += sx
            if e2 < dx:
                error += dx
                y_offset += sy
    pygame.display.flip()
