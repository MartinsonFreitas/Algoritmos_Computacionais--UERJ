def imc(peso, altura):
    '''
    Argumentos: peso, altura: valores flutuantes

    Retorna a classificação conforme tabela abaixo:
        Menor que 18,5 - Abaixo do peso
        Entre 18,5 e 25 - Peso Ideal
        Entre 25 e 30 - Pré-obeso
        Entre 30 e 35 - Obeso grau 1
        Entre 35 e 40 - Obeso grau 2
        Acima de 40 - Obeso grau 3

    '''
    # Calcular IMC
    # Calcular IMC =  peso / (altura ** 2)
    imc = peso/(altura*altura) # ou imc = peso / (altura ** 2)
    
    if (imc < 18.5):
        return('abaixo do peso ideal.')
    elif ((imc >= 18.5) and (imc < 25.0)):
        return('com o peso normal.')
    elif ((imc >= 25.0) and (imc < 30.0)):
        return('com excesso de peso.')
    elif ((imc >= 30.0) and (imc < 35.0)):
        return('com obesidade grau 1.')
    elif ((imc >= 35.0) and (imc < 40.0)):
        return('com obesidade grau 2.')
    else:
        return('com obesidade grau 3.')
       
def main_imc():
    # 1º: Receber as váriaveis:
    # Altura
    altura = float(input("Insira sua altura (X.XX metros):"))
    # Peso
    peso = float(input("Insira seu peso (XXX.XX Kg):"))
    
    # processamento
    calcula_imc = imc(peso, altura)
    
    #saída
    print('Você está', calcula_imc)
