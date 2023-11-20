"""
   Atualmente no Brasil, os números de telefone fixo têm 8 dígitos, 
   enquanto os números de telefone celular têm 9 dígitos. 
   
   Esses números são regionais, então, para completar a identificação do usuário no Brasil com base em um número, 
   também é importante considerar o código de área (DDD), composto por 2 dígitos. 
   
   É comum as pessoas fornecerem seu número telefônico tanto incluindo o código de área quanto não incluindo.

    Seguindo apenas essas regras de tamanho, alguns exemplos de números de telefone válidos no Brasil são:
        21912316165
        1132316165
        71912316165
        323231616
        32316165
        912316165
        
    Faça uma função que receba como entrada uma string contendo uma sequência de dígitos, 
    que supostamente corresponde ao número de telefone informado por um usuário 
    (parta do princípio de que essa string só contém dígitos). 
    
    Sua função deve identificar se o número de telefone é válido no Brasil, ou seja, 
    se ele se encaixa em um dos padrões aceitáveis. 
    
    Caso seja válido, sua função deve retornar uma tupla com duas strings: 
    a primeira contendo exatamente dois dígitos correspondentes ao DDD 
    (ou uma string vazia, caso o DDD não tenha sido informado), 
    e a segunda contendo 8 ou 9 dígitos correspondentes ao número de telefone sem o DDD.
    
    Caso o número seja inválido, sua função deve retornar uma tupla com duas strings vazias
"""

def valida_telefone(tel):
    if len(tel) == 8:
        ddd = []
        telefone = tel[:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 9:
        ddd = []
        telefone = tel[:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 10:
        ddd = tel[:2]
        telefone = tel[2:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 11:
        ddd = tel[:2]
        telefone = tel[2:]
        #tel_valido = (ddd, telefone)
    else:
        ddd = []
        telefone = []
        #tel_valido = (ddd, telefone)
    
    tel_valido = (ddd, telefone) 
    
    return tel_valido

#Função main
def main():

    # entrada de dados    
    tel = input("Digite o número de telefone válido DDNNNNNNNNN: ")
               
    # saida
    print(valida_telefone(tel))
    
#Testando a função
main()