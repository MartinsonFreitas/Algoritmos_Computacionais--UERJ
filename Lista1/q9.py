"""
    Escreva uma função que receba um número inteiro positivo como argumento e verifique se é um número perfeito. 
    Um número perfeito é aquele que é igual à soma de seus divisores próprios (excluindo ele mesmo).
    
    ▪ Exemplos de números perfeitos
    ➢ O número 6 é um número perfeito, pois a soma de seus divisores próprios (1, 2, 3) é igual a ele mesmo: 
        1 + 2 + 3 = 6.
    ➢ O número 28 é um número perfeito, pois a soma de seus divisores próprios (1, 2, 4, 7, 14) é igual a ele 
        mesmo: 1 + 2 + 4 + 7 + 14 = 28.    
"""

def perfeito(n):    
    soma = 0
    
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor # soma = soma + divisor
            
    if n == soma:
        return True
    else: 
        return False
        
#n = int(input("Digite o valor de n: "))
n = 29
result = perfeito(n)
print(result)