def imprime_matriz(n):
    i = 1
    while i<=n:
        j=0
        while j < i:
            print('* ', end='')
            j+=1
        print()
        i+=1

import turtle as t

def desenha_ponto(x,y):
    t.goto(x,y)
    t.down()
    t.dot()
    t.up()

def desenha_matriz(n):
    t.color('red')
    #t.speed(10)
    i=0
    while i < n:
        j=0
        while j < n:
            desenha_ponto(i*20,j*20)            
            j+=1
        i+=1

def desenha_matriz_cor(n):
    i = 0
    while i < n:
        j=0
        while j < n:
            if i < j:
                t.color('blue')
            else:
                t.color('red')
            desenha_ponto(i*-20,j*20)
            j+=1
        i+=1
    t.done()

#Função main
def main():
    # entrada de dados    
    numero = int(input('digite o número para a matriz: '))
          
    # processamento
    #imprime_matriz(numero)
    desenha_matriz_cor(numero)
               
    # saida

#Testando a função
main()