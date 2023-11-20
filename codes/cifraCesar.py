def cifraCesar(texto):
    """
    Crie uma função cifrar_texto(texto, chave) que cifre um texto usando a Cifra de César. A cifra deve deslocar
    cada letra do texto original para a direita de acordo com o valor da chave. Por exemplo, se a chave for 3, a
    letra 'a' será substituída por 'd', 'b' por 'e', e assim por diante.

    Args:
        texto (string): Recebe um texto

    Returns:
        string: Criptografa o texto usando a Cifra de César
    """

    resultado = ""
    tamanho = len(texto)
    i = 0
    while i < tamanho:
        resultado += texto[i] # Adiciona o caractere atual ao resultado
        # Verifica se o próximo caractere é igual ao atual
        while i < tamanho - 1 and texto[i] == texto[i + 1]:
            i += 1 # Se for igual, avança para o próximo caractere

        i += 1 # Passa para o próximo caractere

    return resultado

MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def cesar(data, key, mode):
    # tupla com as letras do alfabeto
    alfabeto = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'
    novo_texto = ''
    for c in data:
        indice = alfabeto.find(c)
        if indice == -1:
            novo_texto += c
        else:
            novo_indice = indice + key if mode == MODE_ENCRYPT else indice - key
            novo_indice = novo_indice % len(alfabeto)
            novo_texto += alfabeto[novo_indice:novo_indice+1]
    return novo_texto

# Tests
key = 3
original = 'Olá Mundo zçÇ'
print('  Original:', original)
cifrado = cesar(original, key, MODE_ENCRYPT)
print('Encriptada:', cifrado)
plain = cesar(cifrado, key, MODE_DECRYPT)
print('Decriptada:', plain)