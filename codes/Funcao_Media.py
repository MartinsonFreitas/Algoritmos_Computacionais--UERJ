def calcula_media(x,y):
    '''Função que calcula a média de dois números a e b'''
    media = (x+y)/2
    return  media# Retorna a media de x e y dividido por 2

#Função main
def main():
    # entrada de dados
    n1 = float(input('Insira a nota 1: '))
    n2 = float(input('Insira a nota 2: '))
    proj = float(input('Insira a nota do Projeto: '))
    
    # processamento
    notaFinal = calcula_media(calcula_media(n1,n2), proj)
    
    # saida
    print('A nota final é: ', notaFinal)
    
#Testando a função
main()