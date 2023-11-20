# Criar uma função que calcula a área de um anel de raios r1 e r2
def areaCirculo(r):
    '''Retorna a area de um Círculo de Raio R'''
    areaCircular = (3.14)*(r**2)
    
    return areaCircular

def areaAnel(r1, r2):
    """Função que cria a área de um anel de raiz de r1 e r2, onde r1>r2"""
    return areaCirculo(r1) - areaCirculo(r2)
    
#Função main
def main():
    # entrada de dados
    #R1 = float(input('Insira o valor do raio do Anel externo: '))
    #R2 = float(input('Insira o valor do raio do Anel interno: '))
      
    # processamento
    #area1 = areaCirculo(3)
    #area2 = areaCirculo(5)
    #areaAnel = area2-area1
    
    r1 = 5
    r2 = 3
           
    # saida
    print('A área do anel é: ', areaAnel(r1, r2))
    # ou
    #print('A área do anel é: ', areaAnel(5, 3))
    
#Testando a função
main()