"""
    Faça uma função chamada 'repetidos' que receba como entrada uma lista de números e retorne o número de vezes 
    que um elemento da lista é igual ao elemento anterior.
    
    Exemplo: repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7])
    Resposta: 6
"""

def repetidos(l):
    conta = 0
        
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            conta += 1
    
    return conta

l = [1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7, 7]

result = repetidos(l)
print(result)