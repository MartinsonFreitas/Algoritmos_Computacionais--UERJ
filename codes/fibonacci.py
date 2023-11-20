def fibonacci(n):
    """
    Esta função solicita um número inteiro positivo ao usuário e imprime
    os primeiros n números da série de Fibonacci.
    """

    # Inicialização dos primeiros dois números da série
    num1, num2 = 0, 1
    next_num = num1 + num2

    # Imprime os primeiros n números da série
    contador = 0
    print(num1, num2)
    while contador < n:
        print(num1, num2, next_num)
        num1, num2 = num2, num1 + num2
        next_num = num1 + num2
        contador += 1

#Função main
def main():
    # entrada de dados    
    numero = int(input('digite o número para a função fibonacci: '))
          
    # processamento
    fibonacci(numero)
               
    # saida

#Testando a função
main()