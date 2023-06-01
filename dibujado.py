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


