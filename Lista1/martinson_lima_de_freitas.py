#----------------------------------------- Questão 1 ----------------------------------------
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

#teste
#imc(82.5 , 1.68)

#----------------------------------------- Questão 2 ----------------------------------------
def operacao(t):
    ''' Recebe uma tupla com dois números (x,y) e uma operação 
    
        Retorna o resultado da operação selecionada  
    '''
    x = t[0]
    y = t[1]
    op = t[2]
    #print(x,y, op.lower())
    
    operacao = op.lower()
    
    if (operacao == 'soma'):
        result = x + y
    elif (operacao == 'mult'):
        result = x * y
    elif (operacao == 'div'):
        result = x / y
    elif (operacao == 'sub'):
        result = x - y
    elif (operacao == 'mod'):
        result = x % y
    elif (operacao == 'pot'):
        result = x ** y
    else:
        result = 'A operação informada não foi reconhecida!'
        
    return result

#teste
#t = (1, 2, 'SOMA')
#operacao(t)

#----------------------------------------- Questão 3 ----------------------------------------
def trocar_vogais(texto):
    """Recebe um texto e troca as vogais por 'i'

    Args:
        texto (string): Texto fornecido pelo usuário

    Returns:
        texto (string): Texto com as vogais trocadas por 'i'
    """
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

#teste
#trocar_vogais('Isto e um teste de entrada de dados para trocar as vogais por i')

#----------------------------------------- Questão 4 ----------------------------------------
def valida_telefone(tel):
    """Validação de telefone fornecido com 'DDD' ou 'Sem' de Telefone Fixo ou Celular 

    Args:
        Recebe uma string contendo uma sequência de dígitos, que supostamente corresponde ao número de telefone.

    Returns:
        Tupla com duas strings: dois dígitos correspondentes ao DDD ou uma string vazia, 
        caso o DDD não tenha sido informado, a segunda contendo 8 ou 9 dígitos correspondentes
        ao número de telefone sem o DDD.
    
        Caso o número seja inválido, retorna uma tupla com duas strings vazias
    """
    if len(tel) == 8:
        ddd = []
        telefone = tel[:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 9:
        ddd = []
        telefone = tel[:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 10:
        ddd = tel[:2]
        telefone = tel[2:]
        #tel_valido = (ddd, telefone)
    elif len(tel) == 11:
        ddd = tel[:2]
        telefone = tel[2:]
        #tel_valido = (ddd, telefone)
    else:
        ddd = []
        telefone = []
        #tel_valido = (ddd, telefone)
    
    tel_valido = (ddd, telefone) 
    
    return tel_valido

#teste
#valida_telefone(2199999999)

#----------------------------------------- Questão 5 ----------------------------------------
def media(t):
    """Recebe uma tupla contendo 4 informações: o nome do aluno e três notas

    Args:
        t (_tupla_): <Nome>:str, <nota1>:float, <nota2>:float, <nota3>:float
        
    Returns:
        Retorna uma tupla, cujo primeiro elemento é o nome do aluno, 
        o segundo elemento é a média e o terceiro elemento é a situação do aluno, representada por uma string.
    
        Se a média das três notas do aluno for maior ou igual a 7 (inclusive), a função deverá retornar: 
        (<nome>, <media>, 'aprovado, Parabéns!'). 
    
        Se a média do aluno for menor que 7, porém maior ou igual a 5, a função deve retornar: 
        (<nome>, <media>, 'aprovado'). 
    
        Se a média for menor que 5, a função deve retornar: 
        (<nome>, <media>, 'reprovado'). 
    """
    nome = t[0]
    x = t[1]
    y = t[2]
    z = t[3]
    media = round((x+y+z)/3, 1)
    # Mensagem da Situação do aluno de acordo com a média
    if (media >= 7):
        msg = (nome, media, 'Aprovado, Parabéns!')
    elif(media >= 5):
        msg = (nome, media, 'Aprovado!')
    else:
        msg = (nome, media, 'Reprovado!')
        
    print (msg)  
   
#teste 
#t = ('Marcio', 7.9, 6.5, 8.2)
#media(t)

#----------------------------------------- Questão 6 ----------------------------------------
def colisao(t1, t2):
    """Função determine se dois retângulo se interceptam.  Cada retângulo é determinado pelas coordenadas x e y 
    de dois de seus vértices diametralmente opostos. Os lados de cada retângulo são sempre paralelos aos eixos x e y.
    Args:
        Os parâmetros de entrada são duas tuplas com quatro valores inteiros cada uma
        t1 (_tupla_): representando as coordenadas do primeiro retângulo
        t2 (_tupla_): representa as coordenadas do segundo retângulo.    
    Returns:
        Retornar o valor booleano True caso haja interseção ou False caso não haja.
    
    """
    
    # indicando os vértices do primeiro retângulo
    x1 = int(t1[0])
    y1 = int(t1[1])
    l1 = int(t1[2])
    a1 = int(t1[3])    
    # indicando os vértices do segundo retângulo
    x2 = int(t2[0])
    y2 = int(t2[1]) 
    l2 = int(t2[2])
    a2 = int(t2[3])    
    # verificar colisão
    # se coordenada do vértice do retângulo estiver entre
    if ( (x1 < (x2 +l2) ) and ( (x1 +l1) > x2) and (y1 < (y2 + a2) ) and ( (y1 +a1) > y2) ):    
       return True
    else:
        return False    

#teste
#t1 = (0,0,2,2)
#t2 = (1,1,3,3)
#result = colisao(t1, t2)
#print(result)

#----------------------------------------- Questão 7 ----------------------------------------
def maiores_que(l, n):
    """
    Função recebe uma lista de números inteiros e um número inteiro 'n'. 

    Args:
        l (_list_): lista de números inteiros.
        n (_int_): número inteiro

    Returns:
        Retornaa outra lista contendo todos os números da lista original que são maiores que 'n', 
        ordenados em ordem crescente.
    """
    nl = []
    #tamanho = len[l]
    
    for i in range(len(l)):
        if l[i] > n:
            nl.append(l[i])
    
    return sorted(nl)

#teste
#l = [4, 5, 2, 1, 10, 6, 3, 7, 6, 9]
#n = 5
#result = maiores_que(l, n)
#print(result)

#----------------------------------------- Questão 8 ----------------------------------------
def repetidos(l):
    """Função chamada 'repetidos' que receba como entrada uma lista de números e retorne o número de vezes 
    que um elemento da lista é igual ao elemento anterior.

    Args:
        l (_lista_): lista de números

    Returns:
        _Inteiro_: retorne o número de vezes que um elemento da lista é igual ao elemento anterior
    """
    conta = 0
        
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            conta += 1
    
    return conta

# teste
#l = [1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7, 7]
#result = repetidos(l)
#print(result)

#----------------------------------------- Questão 9 ----------------------------------------
def perfeito(n):
    """Função que receba um número inteiro positivo como argumento e verifique se é um número perfeito.

    Args:
        n (_int_): Número inteiro

    Returns:
        _Booleano_: True ou False
    """

    soma = 0
    
    for divisor in range(1,n):
        if n % divisor == 0:
            soma += divisor # soma = soma + divisor
            
    if n == soma:
        return True
    else: 
        return False
 
# teste       
#n = int(input("Digite o valor de n: "))
#n = 29
#result = perfeito(n)
#print(result)

#----------------------------------------- Questão 10 ----------------------------------------
def investe(dados):
    """Função calcula e imprime a quantia na conta ao final de cada ano, ao longo de n anos. 
    De acordo com a seguinte fórmula para determinar estas quantias: a = p(1 + r)n
    
    Args:
        dados = [p, r, n]
        p é a quantia investida originalmente (i.e., o valor principal)
        r é a taxa anual de juros.
        n é o número de anos
        a é a quantia existente em depósito no final do n-ésimo ano
    """

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

"""
Teste
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
"""