'''
    Escreva uma função que receba dois parâmetros: uma tupla com dois números e uma string. De acordo com a string
    recebida, e com a Tabela, a função deve realizar diferentes operações com os números e retornar o resultado. 
    Obs. No caso de a string de entrada ser diferente das strings da Tabela, 
    a função deve retornar uma string com a seguinte mensagem: A operação informada não foi reconhecida.
    
    SOMA = soma de dois números
    MULT = multiplicação de dois números
    DIV = divisão de dois números
    SUB = subtração de dois números
    MOD = retorna o resto da divisão do primeiro pelo segundo
    POT = retorna o primeiro elevado pelo segundo
'''

def operacao(t):
    ''' Recebe uma tupla com dois números (x,y) e uma operação, retorna o resultado da operação  
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
        
    print(result)
    
t = (1, 2, 'POTAGE')
operacao(t)