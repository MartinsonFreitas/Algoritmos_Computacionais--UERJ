def somaPrimos(n):
    """
        leia um número N e some os primeiros números primos.
    """
    soma=0

    if n >= 1:
        soma = soma +  2
        p = 1
        y = 3
        while y <= n:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                soma = soma + x
                p = p + 1
                
            y = y + 2

    print("A soma dos números primos até", n, "é", soma)
    
    #print("A soma dos", n,"números primos é", soma)

def eh_primo(n):
    """
        verifica se um numero é primo
    """
    divisores = 0
    i = 1

    while i<=n:
        if n % i ==  0:
            divisores+=1
        i+=1

    if divisores == 2:
        return True
    else:
        return False

import math
def eh_primo_v2(n):
    """
        verifica se um numero é primo
    """
    i = 2

    if n > 1:
        return True
    else:
        return False

    while i< math.sqrt(n):
        if n % i ==  0:
            return False
        i+=1

    return True

def soma_primos(n):
    """
        Soma os números primos menores a n 
    """
    i=2
    soma = 0
    while i < n:
        if eh_primo_v2(i):
            soma+=i
            print(i)
        i+=1
    return soma
    
      
#Função main
def main():

    # entrada de dados    
    n = int(input("Digite um número: "))
          
    # processamento
    if n < 0:
        print("Número inválido. Digite apenas valores positivos")
    else:
        somaPrimos(n)

   
               
    # saida

#Testando a função
main()



