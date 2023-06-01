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

#Funcion de selección de comandos
def procesar_comando(comando):
    global color, thickness  # Variables locales utilizadas por todo el código
    partes = comando.strip().split()
    if len(partes) > 0 and partes[0] == "/help": #Desgliega en la termimal los comandos para ejecutar
        help.ayuda()
    elif len(partes) > 0 and partes[0] == "linea": 
        if partes[1] == "=": #Dibuja en pantalla una linea con los puntos de incio y fin
            x1, y1, x2, y2 = map(int, partes[2:])
            dibujado.linea(surface, color, x1, y1, x2, y2)
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "figura":
        if partes[1] == "-circulo": #Dibuja un circulo con los puntos de origen y el radio de este
            centro_x, centro_y, radio = map(int, partes[2:])
            dibujado.circulo(surface, color, centro_x, centro_y, radio)
        elif partes[1] == "-triangulo": #Dibuja un triangulo dando los tres puntos de este, para unirlos con lineas
            if len(partes) == 8:
                x1, y1, x2, y2, x3, y3 = map(int, partes[2:])
                dibujado.triangulo(surface, color, x1, y1, x2, y2, x3, y3)
        elif partes[1] == "-cuadrado": #Dibuja en pantalla un cuadrado con las coordenadas y el tamaño de lado
            x, y, lado = map(int,partes[2:])
            dibujado.cuadrado(surface, color, x, y, lado)
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "-color": 
        if partes[1] == "ls": #Despliega una lista con los colores disponibles a elegir
            colores.lista()
        elif partes[1] == "set": #Selecciona el color que el usuario elija
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
    elif len(partes) > 0 and partes[0] == "-fondo": #Con los colores predefinidos cambia el color del fondo
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
    elif len(partes) > 0 and partes[0] == "-grosor": #Aumetna el grosor de los pixeles generados
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

#Abre el archivo .cmd en donde se estarán guardando los comandos que elija el usuario
myfile = open("comandos.cmd", "r")
for cmd in myfile:
    cmd = cmd.strip()
    procesar_comando(cmd)
    print(f"-{cmd}-")
myfile.close()

#Bucle que mantiene a la ventana del programa abierta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
