import turtle as t
from random import randint

def desenha_aleatorio(n,cor='green'):
    '''desenha aleatoriamente'''
    t.shape('turtle')
    t.color(cor)
    distancia_total = 0
    
    for i in range(n):
        angulo = randint(-60,60)
        distancia = randint(0,10)
        t.left(angulo)
        t.forward(distancia)
        distancia_total += distancia
        
    
    t.write(distancia_total, font=('Arial', 12, 'bold'))
    t.done()
    
#principal

desenha_aleatorio(100)