"""_summary_
O imposto de renta IR depende de uma tabela dividida em quatro faixas de renda, com uma alíquota
progressiva que vai de 7,5% a 27,5%. A faixa máxima atinge os salários acima de R$ 4.664,68.

    Faixas e as respectivas alíquotas
        • Faixa 1: Até R$ 1.903,98: isento
        • Faixa 2: De R$ 1.903,98 até R$ 2.826,65: 7,5%
        • Faixa 3: De R$ 2.826,66 até R$ 3.751,05: 15%
        • Faixa 4: De R$ 3.751,06 até R$ 4.664,68: 22,5%
        • Faixa 5: Acima de R$ 4.664,68: 27,5%
        
    • Por exemplo, um contribuinte com renda mensal tributável no valor de R$5000,00 pagará R$505,64 de imposto de
        renda, calculado da forma descrita na Tabela:
        
        Faixa de Base de Cálculo    Alíquota    Valor do Imposo (R$)
        1ª Faixa: R$ 1903,98        Isento      00,00
        2ª Faixa: R$ 922,67         7,5%        69,20
        3ª Faixa: R$ 924,40         15%         138,66
        4ª Faixa: R$ 913,63         22,5%       205,57
        5ª Faixa: R$ 335,32         27,5%       92,21
        Total: 5000,00              10,11%      505,64
            
    Nesse caso, a alíquota efetiva (percentual final do imposto incidente sobre o rendimento do contribuinte) foi de
    10,11% (= 505,64/5000,00)
"""

def IR (salario):
    """
    Recebe o valor do Salário e calcula a alíquota do Imposto de Renda

    Parâmetro:
        salario_tributavel (float): salário
        
    Retorna:
    float: desconto_IR
        Faixas e as respectivas alíquotas
            Faixa 1: Até R$ 1.903,98: isento
            Faixa 2: De R$ 1.903,99 até R$ 2.826,65: 7,5%
            Faixa 3: De R$ 2.826,66 até R$ 3.751,05: 15%
            Faixa 4: De R$ 3.751,06 até R$ 4.664,68: 22,5%
            Faixa 5: Acima de R$ 4.664,68: 27,5%
    """
    
    if salario > 4664.68: # Faixa 5
        IR_Faixa5 = (salario - 4664.68) * 0.275
        desconto_IR = IR_Faixa5 + 413.43 
    elif salario > 3751.06:  # Faixa 4
        IR_Faixa4 = (salario - 3751.06) * 0.225
        desconto_IR = IR_Faixa4 + 207.86
    elif salario > 2826.66: # Faixa 3
        IR_Faixa3 = (salario - 2826.66) * 0.15
        desconto_IR = IR_Faixa3 + 69.20 
    elif salario > 1903.99: # Faixa 2
        IR_Faixa2 = (salario - 1903.99) * 0.075
        desconto_IR = IR_Faixa2 
    else: # Faixa 1
        desconto_IR = 0
        
    return desconto_IR

#Função main
def main():
    # entrada de dados
    salario = float(input('Insira o valor do salário: '))    
      
    # processamento
    desconto = IR(salario)
    aliquota_IR = (desconto/salario)
           
    # saida
    print(f'O desconto do IR é: R$ {desconto:,.2f}')
    print(f'A aliquota do IR é: {aliquota_IR:,.2%}')
    
#Testando a função
main()