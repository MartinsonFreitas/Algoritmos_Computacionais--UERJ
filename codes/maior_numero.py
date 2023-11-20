def maior_numero(num1, num2):
    """
    Retorna o maior número entre dois.

    Argumentos:
    num1 -- o primeiro número (int ou float)
    num2 -- o segundo número (int ou float)

    Retorna:
    O número maior entre num1 e num2 (int ou float)
    """
    if num1 > num2:
        return num1
    else:
        return num2
    
def principal():
    # entrada de dados
    n1 = float(input("Insira o número 1: "))
    n2 = float(input("Insira a número 2: "))

    # processamento
    maior = maior_numero(n1, n2)
    #saida
    print('O maior número é',maior)

#chamada principal
principal()