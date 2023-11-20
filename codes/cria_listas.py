import turtle as t

def cria_listas():
    P = []
    Q = []
    
    for i in range(-300, 300, 50):
        P.append((i, 100))
        Q.append((i,-100))
        
    return P,Q

def desenha_pontos(P,Q):
    t.up()
    t.color('red')
    for ponto in P:
        t.goto(ponto)
        t.dot(10)
        
    t.color('blue')
    for ponto in Q:
        t.goto(ponto)
        t.dot(10)
        
    t.done()
    
def desenha_pontos_zip(P,Q):
    t.up()
    for p,q in zip(P,Q):
        t.color('red')
        t.goto(p)
        t.dot(10)
        t.down()
        t.color('blue')
        t.goto(q)
        t.dot(10)            
        
    t.done()
    
#principal
P,Q = cria_listas()
#desenha_pontos(P,Q)
desenha_pontos_zip(P,Q)