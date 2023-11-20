# Criar uma função que calcula a área de um círculo de rai R
def calcula_area_circulo(r):
    '''Retorna a area de um Círculo de Raio R'''
    areaCircular = (3.14)*(r**2)
    
    return areaCircular

#Função main
def main():
    # entrada de dados
    R = float(input('Insira o valor do raio do Circulo: '))    
      
    # processamento
    area = calcula_area_circulo(R)
           
    # saida
    print('A área do círculo é: ', area)
    
#Testando a função
main()