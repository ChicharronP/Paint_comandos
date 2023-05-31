
def ayuda():
    print("Lista de comandos: \n")
    print("'linea -h' 'coordenada x de inicio' 'coordenada x de fin' 'coordenada en el eje y' genera una linea horizontal")
    print("'linea -v' 'Coordenada y del inicio' 'coordenada y de fin'  'coordenada en el eje x' genera una linea vertical")
    print("'linea -d' 'coordenada x inicial' 'coordenada y inicial' 'coordenada x final' 'coordenada y final' genera una linea diagonal")
    print("'color ls' genera una lista con los colores disponibles para dibujar")
    print("'color set 'NOMBRE_COLOR' cambia el color con el que se generan los trazos")
    print("-fondo 'Nombre_COLOR' cambia el color del fondo")
    print("'-grosor' 'NUM_PIXELES' cambia el grosor de los trazos siempre y cuando el valor sea mayor a 1")