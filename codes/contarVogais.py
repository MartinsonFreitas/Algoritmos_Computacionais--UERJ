def contarVogais(texto): 
    """
        Conta o número de vogais presentes em uma string.
    """

    texto = texto.lower() # Converter a string para minúsculas
    vogais = "aeiouéíóãê"
    contador = 0
    i=0
    n = len(texto)

    while i < n:
        if texto[i] in vogais:
            contador += 1
        i+=1

    return contador

def remover_vogais(texto):
    texto = texto.lower() # Converter a string para minúsculas
    vogais = "aeiou"
    saida = ''
    
    i=0
    n = len(texto)

    while i < n:
        if texto[i] not in vogais:
            saida += texto[i]            
        i+=1

    print('O novo texto sem as vogais é:"', saida,'"')
    #return saida

def trocar_vogais(texto):
    texto = texto.lower() # Converter a string para minúsculas
    vogais = "aeiou"
    saida = ''
    
    i=0
    n = len(texto)

    while i < n:
        if texto[i] not in vogais:
            saida += texto[i]
        else:
            saida += 'i'       
        i+=1

    #print('O novo texto sem as vogais é:"', saida,'"')
    return saida

def inverter_string(texto):
    texto = texto.lower() # Converter a string para minúsculas
    saida = ''
    i = len(texto)-1

    while i >= 0:
        saida += texto[i]            
        i-=1

    return saida

    #print('O texto invertido é:"', saida,'"')


def validaPalindromo(texto):
    """
        Valida se o texto é um palindromo
    """

    if texto == inverter_string(texto):
        return True
    else:
        return False
    
def remover_espacos(texto):
    """
        Remove os espaçoes em branco
    """
    saida = ''
    i = 0

    while i < len(texto):
        if texto[i] != ' ':
            saida += texto[i]
        i += 1

    return saida

def encontraPalavra(texto, palavra):
    """
        Encontra uma plavra num texto
    """
    texto = texto.lower() # Converter a string para minúsculas
    palavra = palavra.lower() 
    cont = 0
    i=0
    j=0
       
    c = len(texto)
    n = len(palavra)

    while i < c:        
        if texto[i] in palavra[j]:
            while j < n:
                if j == n:
                    cont +=1
            j+=1           
            i+=1            
        else:
            i+=1
            j=0

    return cont

     
#Função main
def main():

    # entrada de dados    
    texto = input("Digite aqui seu texto: ")
    #palavra = input("Digite a palavra a ser procurada no texto: ")
          
    # processamento
    #nVogais = contarVogais(texto)
               
    # saida
    #print('O número de vogais no seu texto é', nVogais)
    #remover_vogais(texto)
    print(trocar_vogais(texto))
    #inverter_string(texto)
    #print(validaPalindromo(texto))s
    #print(remover_espacos(texto))
    #print(encontraPalavra(texto,palavra))

#Testando a função
main()