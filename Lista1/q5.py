"""
    Faça uma função em Python, que receba uma tupla contendo 4 informações: o nome do aluno e três notas. 
    
    Sua função deve retornar uma tupla, cujo primeiro elemento é o nome do aluno, 
    o segundo elemento é a média e o terceiro elemento é a situação do aluno, representada por uma string.
    
    Se a média das três notas do aluno for maior ou igual a 7 (inclusive), a função deverá retornar: 
        (<nome>, <media>, 'aprovado, Parabéns!'). 
    
    Se a média do aluno for menor que 7, porém maior ou igual a 5, a função deve retornar: 
        (<nome>, <media>, 'aprovado'). 
    
    Se a média for menor que 5, a função deve retornar: 
        (<nome>, <media>, 'reprovado'). 
        
    A média deve ser retornada com uma casa decimal apenas.
"""

def media(t):
    nome = t[0]
    x = t[1]
    y = t[2]
    z = t[3]
    media = round((x+y+z)/3, 1)
    
    if (media >= 7):
        msg = (nome, media, 'Aprovado, Parabéns!')
    elif(media >= 5):
        msg = (nome, media, 'Aprovado!')
    else:
        msg = (nome, media, 'Reprovado!')
        
    print (msg)  
    
# teste Q05 #
t = ('Marcio', 7.9, 6.5, 8.2)
media(t)