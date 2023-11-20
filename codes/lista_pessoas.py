L = [['João da Silva', 28, 2500.0],
     ['Maria Eduarda', 32, 2800.0],
     ['Pedro Enriaue', 25, 1600.00],
     ['Paulo Caio', 50, 4100.0],
     ['Ana Paula', 27, 3200.00],
     ]

P = ['Enrique', 43, 3200.0]

def media_salarial(L):
    """Calcular a média salarial, utilizar o comando for
    Argumentos
        lista de pessoas
    Saída
        Média salarial: float
    """
    soma=0
    quantidade = len(L)
    
    for pessoa in L:
        salario = pessoa[2]
        soma += salario
        
    return soma/quantidade

def bonificar(L, nome):
    """Bonifica 10% ao salário de uma pessoa, caso exista
    Argumentos
        lista de pessoas com elementos [nome, idade, salario]
        nome: nome da pessoa a bonificar
    Saida:
        lista modificada
    """
    i = 0
    while i < len(L):
        if L[i][0].lower() == nome.lower(): #achou
            L[i][-1] = L[i][-1]*1.1
            return
        i+=1
    print('Pessoa não existe')
    
def remover(L, nome):
    """Remove uma pessoa, caso exista"""
    i = 0
    while i < len(L):
        if L[i][0].lower() == nome.lower(): #achou
            del L[i]
            return
        i+=1
    print('Pessoa não existe')

def inserir_ordenador(L, p):
    """Insere uma pessoa, caso exista"""
    i = 0   
    while i < len(L) and p[0].lower() > L[i][0].lower():
       i+=1
    L.insert(i,p)
    
def ordenar_nome(L):
    """Ordenar a lista por ordem alfabética"""
    lista_ordenada = sorted(L)
    
    return lista_ordenada

from operator import itemgetter

def ordenar_idade(L):
    """Ordenar a lista por ordem alfabética"""
    lista_ordenada_idade = sorted(L, key=itemgetter(1))
    
    return lista_ordenada_idade

def ordenar_salario(L):
    """Ordenar a lista por ordem alfabética"""
    lista_ordenada_salario = sorted(L, key=itemgetter(2))
    
    return lista_ordenada_salario

def imprime(L):
    for pessoa in L:
        print(f'Nome:{pessoa[0]}, idade:{pessoa[1]}, salario:{pessoa[2]}')

def menor_salario(L):
    """retorna o menor salário usando a função min"""
    
    menor_salario = L[0][2] #assume o primeiro salário como sendo o menor
    
    for pessoa in L:        
        if pessoa[2] < menor_salario:
            menor_salario = pessoa[2]
        
    return menor_salario
    
def main():
    
    # saida
    print('Menor salario:', menor_salario(L))
    
#Testando a função
main()