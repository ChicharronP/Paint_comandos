class Inicializador:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.surface.fill((255, 255, 255))  # Color de fondo blanco
        pygame.display.flip()