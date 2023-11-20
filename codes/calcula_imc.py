def calcula_imc(imc):
    """
    Escreva uma função que calcule o IMC (Índice de Massa Corporal) de uma pessoa com
    base em sua altura (em metros) e massa (em quilogramas). A função deve retornar uma
    string indicando se a pessoa está abaixo do peso, no peso normal, com sobrepeso ou
    obesa.
    

    """

imc = peso/altura*2

if imc < 18.5:
    return 'Abaixo do peso ideal'
elif 18.5 <= imc < 25:
    return 'Peso ideal'
elif 25 <= imc < 30:
