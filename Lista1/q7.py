"""
Faça uma função chamada 'maiores_que', que recebe uma lista de números inteiros e um número inteiro 'n'. 
A função deve retornar outra lista contendo todos os números da lista original que são maiores que 'n', 
ordenados em ordem crescente.    
"""
  
def maiores_que(l, n):
    nl = []
    #tamanho = len[l]
    
    for i in range(len(l)):
        if l[i] > n:
            nl.append(l[i])
    
    return sorted(nl)

l = [4, 5, 2, 1, 10, 6, 3, 7, 6, 9]
n = 5

result = maiores_que(l, n)
print(result)