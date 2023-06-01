def lista():  # Muestra una lista con los colores disponibles
    lista_colores = {'ROJO': (255, 0, 0), 'VERDE': (0, 255, 0), 'AZUL': (0, 0, 255),
                     'AMARILLO': (255, 241, 61), 'ROSA': (253, 64, 222), 'MORADO': (140, 45, 223),
                     'NARANJA': (234, 141, 59), 'BLANCO': (255, 255, 255), 'NEGRO': (0, 0, 0)}
    print("Lista de colores")
    for color in lista_colores:
        print(color)


def validar_color(color):  # Valida que el color seleccionado se encuentre en la lista
    lista_colores = {'ROJO': (255, 0, 0), 'VERDE': (0, 255, 0), 'AZUL': (0, 0, 255),
                     'AMARILLO': (255, 241, 61), 'ROSA': (253, 64, 222), 'MORADO': (140, 45, 223),
                     'NARANJA': (234, 141, 59), 'BLANCO': (255, 255, 255), 'NEGRO': (0, 0, 0)}
    return color in lista_colores


def obtener_color(color):  # Cambia el color que se haya seleccionado
    lista_colores = {'ROJO': (255, 0, 0), 'VERDE': (0, 255, 0), 'AZUL': (0, 0, 255),
                     'AMARILLO': (255, 241, 61), 'ROSA': (253, 64, 222), 'MORADO': (140, 45, 223),
                     'NARANJA': (234, 141, 59), 'BLANCO': (255, 255, 255), 'NEGRO': (0, 0, 0)}
    return lista_colores[color]






  