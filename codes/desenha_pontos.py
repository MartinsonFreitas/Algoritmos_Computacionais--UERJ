import turtle as t

def desenha_pontos(P, cor):
    """Desenha os pontos de uma lista P"""
    ''' Hello World!'''
    
    t.up()
    t.color(cor)
    for ponto in P:
        t.goto(ponto)
        t.dot(10)
        
    t.done()
        
#Main
P = [(-50,20), (80,-30), (40,15), (10,60)]
desenha_pontos(P, 'red')