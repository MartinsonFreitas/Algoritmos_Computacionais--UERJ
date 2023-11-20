#item a
from math import sqrt
def distancia(P1, P2):
    """Retorna a distancia entre dois pontos
    tuple, tuple ->float"""
    x0, y0 = P1
    x1, y1 = P2
    return sqrt((x0-x1)**2 + (y0-y1)**2)

#item b
def area_triangulo(T):
    """Retorna a ara de um triangulo
    tuple<tuple,tuple,tuple>->float"""
    p1, p2, p3 = T
    a = distancia(p1,p2)
    b = distancia(p1,p3)
    c = distancia(p2,p3)

    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
    
    
