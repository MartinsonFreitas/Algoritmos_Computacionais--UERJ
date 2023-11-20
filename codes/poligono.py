import turtle as t

def quadrado(lado):
    """

    """

def desenha_poligono(lado, n, cor='red'):
    """
    Desenha uma figura usando while

    Argumentos:
    lado: int, número de pixels do lado
    n: número de linhas
    cor: cor da figura
    """
    t.color(cor)
    contador = 1
    while contador <=n:
        t.forward(lado)
        t.left(360/n)
        contador = contador + 1


#Função main
def main():
    # entrada de dados    
    lado = int(input('Insira o comprimento em pixels do lado: '))
    n = int(input('Insira o número de lados: '))
    cor = str(input('Informe a cor desejada: '))
      
    # processamento
    desenha_poligono(lado, n, cor)
               
    # saida


#Testando a função
main()