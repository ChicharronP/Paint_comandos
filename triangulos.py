from dibujado import linea

#Genera un triangulo equilatero a partir de su spawneo y la longitud de sus lados
def equilatero(surface, color, x, y, lado):
    x2 = int(x + lado)
    y2 = int(y)
    x3 = int(x + lado / 2)
    y3 = int(y - (lado * (3**0.5)) / 2)

    #manda a llamar las lineas del triangulo
    linea(surface, color, x, y, x2, y)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x, y)

#genera un triangulo isoceles a partir de su spawneo y la base por la altura de este
def isoceles(surface, color, x, y, base, altura):
    x2 = int(x + base)
    y2 = int(y)
    x3 = int(x + base/2)
    y3 = int(y + altura)

    #manda a dibujar las lineas del triangulo
    linea(surface, color, x, y, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x, y)


#genera un triangulo a partir de sus tres puntos de spawneo
def escaleno(surface, color, x1, y1, x2, y2, x3, y3):
    #manda a dibujar las lineas del triangulo
    linea(surface, color, x1, y1, x2, y2)
    linea(surface, color, x2, y2, x3, y3)
    linea(surface, color, x3, y3, x1, y1)




