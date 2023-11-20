"""
    Crie uma função que receba os 3 lados A, B e C de um triângulo, onde A é o maior lado, e
    retorne em qual caso este triângulo se encaixa.

    • Se A >= B + C, então nenhum triângulo é formado
    • Se A2 = B2 + C2, então temos um triângulo retângulo
    • Se A2 > B2 + C2, então temos um triângulo obtusângulo
    • Se A2 < B2 + C2, então temos um triângulo acutângulo
    
"""

def triangulo(a, b, c) -> str:
    """
    Args:
        a (float): Recebe o valor da medida do lado A do triângulo
        b (float): Recebe o valor da medida do lado B do triângulo
        c (float): Recebe o valor da medida do lado C do triângulo

    Returns:
        str: Mensagem de qual é o tipo de triângulo identificado
    """
    
    if (a >= (b+c)):
        return "Nenhum Triangulo formado!"
    elif  (a**2 == b**2 + c**2):
        return "Triangulo formado é retângulo!"
    elif  (a**2 > b**2 + c**2):
        return "Triangulo formado é obtusângulo!"
    elif  (a**2 < b**2 + c**2):
        return "Triangulo formado é acutângulo!"

#Função main
def main():
    # entrada de dados
    a = float(input('Insira o valor do lado maior do triangulo: '))
    b = float(input('Insira o valor do segundo lado do triangulo: '))
    c = float(input('Insira o valor do terceiro lado do triangulo: '))
      
    # processamento
    msg = triangulo(a,b,c)    
           
    # saida
    print(msg)
        
#Testando a função
main()