def par_impar(num):
    """
    :Verifica se um número é par ou ímpar.

    :Argumentos:
    :num -- o número a ser verificado (int)

    :Retorna:
    :Uma string indicando se o número é par ou ímpar
    """

    if num % 2 == 0:
        return ("O número é par.")
    else:
        return "O número é ímpar."