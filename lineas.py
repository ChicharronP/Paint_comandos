import pygame

width = 800 
height = 600


def linea_h(surface, color):
    for i in range(0, 100):
        surface.set_at((100 + i, 200), color)
    pygame.display.flip()

def linea_v(surface, color):
    for i in range(0, 100):
        surface.set_at((100, 200 + i), color)
    pygame.display.flip()

def superficie(width, height, fill):
    pygame.display.set_mode((width,height))