"""
    Uma pessoa investe uma quantidade (em reais) em uma conta de poupança que rende uma taxa de juros ao ano. 
    Admitindo que todos os juros são deixados em depósito na conta, crie uma função que calcule e imprima a 
    quantia na conta ao final de cada ano, ao longo de n anos. Use a seguinte fórmula para determinar estas 
    quantias: a = p(1 + r)n
    
    Onde:
        • p é a quantia investida originalmente (i.e., o valor principal)
        • r é a taxa anual de juros.
        • n é o número de anos
        • a é a quantia existente em depósito no final do n-ésimo ano
        
    Exemplo de saída para R$1000,00 em 10 anos e 5% (0.05) de juros ao ano
    
    Ano Saldo na conta 
    1   1050.00 
    2   1102.50 
    3   1157.62 
    4   1215.51 
    5   1276.28 
    6   1340.10 
    7   1407.10 
    8   1477.46 
    9   1551.33 
    10  1628.89
"""

def investe(dados):
    # a = p(1 + r)n
    # a é a quantia existente em depósito no final do n-ésimo ano        
    #Exemplo de saída para R$1000,00 em 10 anos e 5% (0.05) de juros ao ano
    
    # p é a quantia investida originalmente (i.e., o valor principal)
    p = dados[0]
    #print(p)
    # r é a taxa anual de juros.
    r = dados[1]
    juros = r/100
    #print(r , juros)
    # n é o número de anos
    n = dados[2]
    #print(n)
    
    a = 0
    
    for i in range(1, n + 1):
        a = round(p*(1 + juros), 2)
        p = a
        print(a)                

# p é a quantia investida originalmente (i.e., o valor principal)
#p = input("Informe o valor do Investimento:")
p = 1000

# r é a taxa anual de juros.
#r = input("Informe a taxa de juros do mercado:")
r = 5

# n é o número de anos
#n = input("Infome o número de anos do Investimento:")
n = 10

dados = [p, r, n]
investe(dados)
