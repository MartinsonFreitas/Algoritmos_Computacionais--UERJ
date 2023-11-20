#a=5
#print(f'O resultado de {a}^3 é: {a**3}')

def soma(a, b):
    '''Função que soma dois números a e b'''
    return a + b

def media(a,b):
    '''Função que calcula a média de dois números a e b'''
    return (a+b)/2 # Retorna a soma de a e b dividido por 2

#Função main
def main():
    a = float(input('Digite um número:'))
    b = float(input('Digite um número:'))
    c = soma (a,b)
    d = media (a,b)
    print('O resultado da soma é:',c)
    print('O resultado da média é:', d)
    
#Testando a função
main()