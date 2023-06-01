# pylint: disable=E1101
# pylint: disable=C0103

import pygame
import dibujado
import colores
import help
import triangulos
import figuras

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800
height = 600
surface = pygame.display.set_mode((width, height))

# Establecer el color predeterminado
color = (0, 0, 255)  # Color azul por defecto
thickness = 1  # Grosor por defecto

# Funcion de selección de comandos
def procesar_comando(comando):
    global color, thickness  # Variables locales utilizadas por todo el código
    partes = comando.strip().split()
    if len(partes) > 0 and partes[0] == "/help":  # Despliega en la terminal los comandos para ejecutar
        help.ayuda()
    elif len(partes) > 0 and partes[0] == "linea":
        if partes[1] == "=":  # Dibuja en pantalla una linea con los puntos de inicio y fin
            x1, y1, x2, y2 = map(int, partes[2:])
            dibujado.linea(surface, color, x1, y1, x2, y2)
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "figura":
        if partes[1] == "-circulo":  # Dibuja un circulo con los puntos de origen y el radio
            centro_x, centro_y, radio = map(int, partes[2:])
            figuras.circulo(surface, color, centro_x, centro_y, radio)
        elif partes[1] == "-cuadrado":  # Dibuja en pantalla un cuadrado con las coordenadas y el tamaño de lado
            x, y, lado = map(int, partes[2:])
            figuras.cuadrado(surface, color, x, y, lado)
        elif partes[1] == "triangulo":
            if partes[2] == "-equilatero":  # Dibuja un triangulo equilatero
                x, y, lado = map(int, partes[3:])
                triangulos.equilatero(surface, color, x, y, lado)
            elif partes[2] == "-isoceles":  # Dibuja un triangulo isoceles
                x, y, base, altura = map(int, partes[3:])
                triangulos.isoceles(surface, color, x, y, base, altura)
            elif partes[2] == "-escaleno":  # Dibuja un triangulo escaleno
                x1, y1, x2, y2, x3, y3 = map(int, partes[3:])
                triangulos.escaleno(surface, color, x1, y1, x2, y2, x3, y3)
            else:
                print(f"Error: Comando desconocido '{comando}'")
        else:
            print(f"Error: Comando desconocido '{comando}'")
    elif len(partes) > 0 and partes[0] == "color":
        if partes[1] == "-ls":  # Despliega una lista con los colores disponibles a elegir
            colores.lista()
        elif partes[1] == "-set":  # Selecciona el color que el usuario elija
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
    elif len(partes) > 0 and partes[0] == "fondo":  # Con los colores predefinidos cambia el color del fondo
        if len(partes) > 1:
            new_color = partes[1]
            if colores.validar_color(new_color):  # Valida que el color escogido por el usuario exista en el programa
                background_color = colores.obtener_color(new_color)
                surface.fill(background_color)  # Llama a la función encargada de colorear el fondo de la ventana
                print(f"Color de fondo cambiado a {new_color}")
            else:
                print(f"Error: El color {new_color} no es válido.")
        else:
            print("Error: Debe proporcionar un color para establecer el fondo.")
    elif len(partes) > 0 and partes[0] == "-grosor":  # Aumenta el grosor de los pixeles generados
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


# Abre el archivo .cmd en donde se estarán guardando los comandos que elija el usuario
with open("comandos.cmd", "r") as myfile:
    for cmd in myfile:
        cmd = cmd.strip()
        procesar_comando(cmd)
        print(f"-{cmd}-")

# Bucle que mantiene la ventana del programa abierta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
