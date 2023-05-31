import pygame 
import dibujado
import colores
import help

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))

# Establecer el color predeterminado
color = (0, 0, 255)  # Color azul por defecto
thickness = 1  # Grosor por defecto

def linea_h(surface, color, x1, x2, y, thickness):
    for t in range(thickness):
        y_offset = y + t  # Aumentar el desplazamiento vertical en cada iteración
        for i in range(x1, x2 + 1):
            surface.set_at((i, y_offset), color)
    pygame.display.flip()

def procesar_comando(comando):
    global color, thickness  # Variables locales utilizadas por todo el código
    partes = comando.strip().split()
    if len(partes) > 0 and partes[0] == "/help":
        help.ayuda()
    elif len(partes) > 0 and partes[0] == "linea":
        if partes[1] == "-h":
            x1, x2, y = map(int, partes[2:])
            dibujado.linea_h(surface, color, x1, x2, y, thickness)
        elif partes[1] == "-v":
            x, y1, y2 = map(int, partes[2:])
            dibujado.linea_v(surface, color, x, y1, y2, thickness)
        elif partes[1] == "-d":
            x1, y1, x2, y2 = map(int, partes[2:])
            dibujado.linea_d(surface, color, x1, y1, x2, y2)
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "-color":
        if partes[1] == "ls":
            colores.lista()
        elif partes[1] == "set":
            if len(partes) > 2:
                new_color = partes[2]
                if colores.validar_color(new_color):
                    color = colores.obtener_color(new_color)
                    print(f"Color cambiado a {new_color}")
                else:
                    print(f"Error: El color {new_color} no es válido.")
            else:
                print("Error: Debe proporcionar un color para establecer.")
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "-fondo":
        if len(partes) > 1:
            new_color = partes[1]
            if colores.validar_color(new_color):
                background_color = colores.obtener_color(new_color)
                surface.fill(background_color)
                print(f"Color de fondo cambiado a {new_color}")
            else:
                print(f"Error: El color {new_color} no es válido.")
        else:
            print("Error: Debe proporcionar un color para establecer el fondo.")
    elif len(partes) > 0 and partes[0] == "-grosor":
        if len(partes) > 1:
            new_thickness = int(partes[1])
            if new_thickness >= 1:
                thickness = new_thickness
                print(f"Grosor cambiado a {thickness}")
            else:
                print("Error: El grosor debe ser un número entero mayor o igual a 1.")
        else:
            print("Error: Debe proporcionar un valor para establecer el grosor.")
    else:
        print(f"Error: Comando desconocido '{comando}'")


myfile = open("comandos.cmd", "r")
for cmd in myfile:
    cmd = cmd.strip()
    procesar_comando(cmd)
    print(f"-{cmd}-")
myfile.close()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
