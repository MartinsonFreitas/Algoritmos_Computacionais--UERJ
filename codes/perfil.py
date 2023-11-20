def perfil_pessoal(dia: int, mes: int, ano: int) -> str:
    """
    O perfil de uma pessoa pode ser determinado a partir da sua data de nascimento,
    conforme exemplificado a seguir. Crie uma função que dada uma data de nascimento,
    retorne o perfil correspondente.

        Exemplo: 13/06/1970

        1) 1306 + 1970 + 3276
        2) 32 + 76 = 108
        3) 108 / 5 = 21 , resto = 3

        R = Perfil
        0 = Tímido
        1 = Sonhador
        2 = Paquerador
        3 = Atraente
        4 = Irresistível

        Argumentos:
        dia: int,
        mes:int,
        ano: int
        Retorna 
        Uma mensagem (str)

    """

    temp1 = (dia*100 + mes) + ano
    temp2 = temp1//100 + temp1%100
    temp3 = temp2% 5


    if temp3 == 0:
        return 'Você é tímido'
    elif temp3 == 1:
        return 'Você é Sonhador'
    elif temp3 == 2:
        return 'Você é atraente'
    elif temp3 == 3:
        return 'Você é atraente'
    else:
        return 'Você é irresistível'

def principal():
    # entrada de dados
    dia = int(input("Digite o dia do seu nascimento XX: "))
    mes = int(input("Digite o mes do seu nascimento XX: "))
    ano = int(input("Digite o dia do seu nascimento XXXX: "))

    # processamento
    perfil = perfil_pessoal(dia, mes, ano)

    #saida
    print('O seu perfil é', perfil)

#chamada principal
principal()

    