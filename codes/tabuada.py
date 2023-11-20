def tabuada(numero):
    """
    Esta função retorna a tabuada de um numero
    """

    mul = 1

    while mul<= 10:
        resultado = numero * mul
        print(f"{numero} x {mul} = {resultado}")
        mul += 1

#Função main
def main():
    # entrada de dados    
    numero = int(input('digite o número para a tabuada: '))
          
    # processamento
    tabuada(numero)
               
    # saida

#Testando a função
main()