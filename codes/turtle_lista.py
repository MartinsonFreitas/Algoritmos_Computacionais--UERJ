import turtle as t

def desenha_lista(L):
    '''Desenha conteúdo de uma lista L com o Turtle'''
    
    for i in range(len(L)):
        texto = str(i)+':'+L[i]
        t.write(texto,  font=('Arial', 10, 'normal'))
        t.forward(70)
        
    t.done()
        
def desenha_lista_tuplas(dados):
    for x, y, fruta in dados:
        t.shape('turtle')
        t.goto(x,y)
        t.write(fruta)
        
    t.done()
    
def desenha_lista_enumeradas(L):
    for i, fruta in enumerate(L):
        texto = str(i)+':'+fruta
        t.write(texto, font=('Arial', 10, 'normal'))
        t.forward(70)
                
    t.done()
        
#principal
L =['Maçã', 'Banana', 'Pera', 'Uva']
dados = [(20,30,'Maçã'), (100,-80, 'Banana'), (-100, -50, 'Uva')]

#desenha_lista(L)
#desenha_lista_tuplas(dados)
desenha_lista_enumeradas(L)