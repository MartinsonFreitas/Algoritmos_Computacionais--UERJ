import turtle as t
def quadrado(lado):
    """
    Desenha uma quadrado usando while
    """
    contador = 1

    while contador <= 4:
        t.forward(lado)
        t.left(90)
        contador = contador + 1

def desenha_poligono(lado, n, cor='red'):
    """
    Desenha uma figura usando while

    Argumentos:
    lado: int, número de pixels do lado
    n: número de linhas
    cor: cor da figura
    """

def desenha_figura(n,x, cor='blue'):
    """
    Desenha figura com n quadrados de lado
    x
    """
    #t.speed('slowly') #velocidade
    t.color('red') # cor da caneta
    contador = 1
    while contador <= n:
        quadrado(x)
        t.left(360/n)
        contador = contador + 1


#Função main
def main():
    # entrada de dados    
    n = int(input('Digite a quantidade de figuras: '))
    x = int(input('Insira o tamanho do lado: '))
    cor = str(input('Informe a cor desejada: '))
      
    # processamento
    desenha_figura(n, x, cor)
               
    # saida


#Testando a função
main()