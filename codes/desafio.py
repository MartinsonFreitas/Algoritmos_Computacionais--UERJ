def IR(salario: float) -> float:
    """
    O importo de renta IR depende de uma tabela dividida em quatro faixas de renda, com uma alíquota
    progressiva que vai de 7,5% a 27,5%. A faixa máxima atinge os salários acima de R$ 4.664,68.

        Faixas e as respectivas alíquotas
        • Faixa 1: Até R$ 1.903,98: isento
        • Faixa 2: De R$ 1.903,99 até R$ 2.826,65: 7,5%
        • Faixa 3: De R$ 2.826,66 até R$ 3.751,05: 15%
        • Faixa 4: De R$ 3.751,06 até R$ 4.664,68: 22,5%
        • Faixa 5: Acima de R$ 4.664,68: 27,5%

    • Por exemplo, um contribuinte com renda mensal tributável no valor de R$5000,00 pagará R$505,64 de imposto de
        renda, calculado da forma descrita na Tabela:

        Faixa 1: 1903,98 --> Isento --> R$ 0,00
        Faixa 2: 922,67 --> 7,5% --> R$ 69,20
        Faixa 3: 924,40 --> 15% --> R$ 138,66
        Faixa 4: 913,63 --> 22,5% --> R$ 205,57
        Faixa 5: 335,32 --> 27,5% --> R$ 92,21
        Total : 5000,00 10,11%  --> R$ 505,64

        • Nesse caso, a alíquota efetiva (percentual final do imposto incidente sobre o rendimento do contribuinte) foi de
        10,11% (= 505,64/5000,00)

    """

    if salario < 1903.98:
        return 0
    elif 1903.98 >= salario < == 2826.65:
        #return (salario - 1903.98) * 0.075
    elif 2826.65 >= salario < == 3751.05:
        #return (salario - 1903.98) * 0.15
    elif 3751.05 >= salario < == 3751.05:
        #return 
    else:
        return 'Você é irresistível'

def principal():
    # entrada de dados
    salario = float(input("Digite o valor do seu salário: xxxx.xx"))

    # processamento
    desconto = IR(salario)

    #saida
    print('O desconto do IR é', desconto)

#chamada principal
principal()
