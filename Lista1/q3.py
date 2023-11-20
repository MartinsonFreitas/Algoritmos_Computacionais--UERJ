"""
Q3. Faça uma função que, dada uma frase, troque todas as vogais das palavras consideradas por i.
Exemplo:
    - Frase lida “Levei meu cachorro para passear”
    - Frase alterada “Livii mii cichirri piri pissiir”
"""

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

#Função main
def main():

    # entrada de dados    
    texto = input("Digite aqui seu texto: ")
               
    # saida
    print(trocar_vogais(texto))
    
#Testando a função
main()