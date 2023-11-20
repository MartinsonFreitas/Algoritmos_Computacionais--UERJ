def tuplaPares(t):
    """
        Retorna os elementos pares de uma tupla
    """
    
    #t = (1,2,3,4,5,6,7,8,9,10)
    
    tpar = ()
    i = 0
    
    while i<len(t):
        if t[i] % 2 == 0:
            tpar += (t[i],) # concatena tupla unitária
        i+=1
        
    return tpar

def tsoma(t):
    """Retorna a soma dos elementos de uma tupla"""
    
    tsoma = 0
    i = 0
    
    while i<len(t):
        tsoma += t[i] # soma
        i+=1
        
    return tsoma
    
def minimo(t):
    """Retorna o menor elemento e a posição de uma tupla de números"""
    tminimo = t[0]
    posicao = 0
    tresult = ()
    i = 1
    
    while i<len(t):
        if t[i] < tminimo:
            tminimo = t[i] # atribui novo valor para minimo
            posicao = i
            
        i+=1
        tresult = (posicao, tminimo)        
    
    return tminimo, posicao
    #return tresult

# Tests
t = (1,2,3,4,5,6,7,8,9,10)

novaTupla = tuplaPares(t)
somaTupla = tsoma(t)
minimoTupla = minimo(t)

x = 1/2+3//3+4**2


#print('  Nova tupla:', novaTupla)
#print('  Soma tupla:', somaTupla)
#print('  Minimo tupla:', minimoTupla)
print(x)