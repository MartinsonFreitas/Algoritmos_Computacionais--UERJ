""" O jogo da forca é um jogo de adivinhação de palavras, onde o jogador tenta descobrir 
a palavra oculta antes de completar o desenho do enforcado, em um número limitado de tentativas.
"""

import random
import turtle

# Configurações básicas do turtle
wn = turtle.Screen() #configurações de tela
turtle.title('Forca')# titulo do grafico
wn.bgcolor("lightyellow") #cor de fundo
t=turtle.Turtle() #t é o cursor do desenho da forca
p=turtle.Turtle() #p cursor da palavra

def caneta():
    """ Configurações da Caneta do Turtle
    """
    p.up()
    p.goto(30,-200)
    p.setheading(0)
    p.pen(pencolor="black", pensize=3, speed=30)

def desenho_da_forca():
    '''função que cria o desenho da forca inicial'''
    #base retangular inicial:inicio(0,0) fim (0,0) 200*50
    t.pen( fillcolor="brown", pensize=3, speed=30)  #alterar a velocidade no final)
    t.begin_fill()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)

    #haste pendurada: (0,0) : (0,-15)
    t.fd(200)
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(250)
    t.up()
    t.end_fill()

    #apoio 45 (0,-25)
    t.goto(0,-60)
    t.down()
    t.begin_fill()
    t.goto(60,-15)
    t.bk(15)
    t.goto(0,-75)
    t.up()
    t.end_fill()

    #corda (150,-15): (150,-40) jump to (30,-200)
    t.goto(150,-17)
    t.pen(pencolor='brown',pensize=2, speed=30)
    t.down()
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.circle(20)
    t.lt(90)
    t._update()

def desenho_da_pessoa(n):
    '''função que desenha o corpo da pessao enforcada membro a membro
        de acordo com a quantidade de erros)'''
    if n==1:
        #cabeça (150,-40) (150,-40 + 2r )
        t.up()
        t.pen(pencolor="brown", fillcolor="pink", pensize=2)
        t.goto(150,-40)
        t.setheading(180)
        t.begin_fill()
        t.down()
        t.circle(20)
        t.up()
        t.end_fill()

    elif n==2:
        #corpo palito
        t.goto(150,-87)
        t.pen(pencolor="pink", fillcolor="pink", pensize=2)
        t.setheading(180)
        t.down()
        t.pensize(15)
        t.lt(90)
        t.fd(45)
        t.up()

    elif n==3:
        #braço esquerdo palito
        t.goto(150,-87)
        t.pen(pencolor="pink", fillcolor="pink", pensize=2)
        t.setheading(270)
        t.down()
        t.pensize(10)
        t.lt(40)
        t.fd(35)
        t.up()
            
    elif n==4:
        #braço direito palito
        t.goto(150,-87)
        t.pen(pencolor="pink", fillcolor="pink", pensize=2)
        t.setheading(310)
        t.down()
        t.pensize(10)
        t.rt(80)
        t.fd(35)
        t.up()

    elif n==5:
        #perna esquerda palito
        t.pen(pencolor="pink", fillcolor="pink", pensize=2)
        t.goto(150,-130)
        t.setheading(230)
        t.down()
        t.pensize(10)
        t.fd(35)
        t.up()
 
    elif n==6:
        #perna direita palito
        t.pen(pencolor="pink", fillcolor="pink", pensize=2)
        t.goto(150,-130)
        t.down()
        t.pensize(10)
        t.setheading(-45)
        t.fd(35)
        t.up()

    elif n==7:
        #morte
        #cabeça (150,-40) (150,-40 + 2r )
        t.up()
        t.pen(pencolor="purple", pensize=2)
        t.color("purple")
        t.setheading(180)
        t.goto(150,-40)
        t.begin_fill()
        t.down()
        t.circle(20)
        t.up()
        t.end_fill()

        # x no olho direito
        t.goto(160,-50)
        t.pen(pencolor="white", pensize=2)
        t.down()
        t.lt(45)
        t.fd(10)
        t.up()
        
        # x no olho esquerdo    
        t.goto(150,-50)
        t.down()
        t.lt(90)
        t.fd(10)
        t.up()
            
        #x olho esquerdo
        t.goto(140,-50)
        t.down()
        t.fd(10)
        t.up()
        # Boca
        t.goto(150,-50)
        t.down()
        t.lt(90)
        t.bk(10)
        t.up()

        t.goto(145,-65)
        t.setheading(0)
        t.down()
        t.fd(15)
        t.up()
        t.color("black")
        t.home()
        
def imprime_mensagem_abertura():
    """ Função de Boas-Vindas no Prompt """
    marcador = "*"
    print(marcador * 38)
    print("*** Prepare-se para ser Enforcado !***")
    print(marcador * 38)
    desenho_da_forca()

def inicializa_letras_acertadas(palavra):
    """ Função que adiciona os espaçoes para cada letra da palavra escolhida """
    return ["_" for letra in palavra]

def pede_chute():
    """ Função que pede a letra a ser inserida """
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    """ Marca a letra em seu devido lugar na palavra """
    index = 0
    p.goto(30,-200)
    
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            
            p.write( f"{letra} ",move=True,font=("",9)) #carrega as letras certas no desenho
        else:
            p.write("     ",move=True,font=("",9)) #carrega as lacunas
        
        index += 1
        p._update()
    p.home()
    
def imprime_mensagem_vencedor():
    """ Imprime a mensagem no Turtle - Vencedor! """
    p.clear()
    p.goto(30,-200)
    p.write("Parabéns, você ganhou!")
    p._update()

def imprime_mensagem_perdedor(palavra_secreta):
    """ Imprime a mensagem no Turtle - Perdedor! """
    p.clear()
    p.goto(30,-200)
    p.write("Puxa, você foi enforcado!")
    p.goto(30,-230)
    p.write(f"A palavra era: {palavra_secreta}")
    p._update()

def desenha_forca(erros): 
    """ Função de iteração a cada erro do Jogador no Turtle """

    if(erros == 1):
        desenho_da_pessoa(1)

    if(erros == 2):
        desenho_da_pessoa(2)

    if(erros == 3):
        desenho_da_pessoa(3)

    if(erros == 4):
        desenho_da_pessoa(4)

    if(erros == 5):
        desenho_da_pessoa(5)

    if(erros == 6):
        desenho_da_pessoa(6)

    if (erros == 7):
        desenho_da_pessoa(7)

def carrega_palavra_secreta():
    """ Carrega a palavra do arquivo anexo para o jogo """
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    #carrega as lacunas da palavra secreta no desenho
    for lacunas in range(len(palavra_secreta)):
        p.write("_  ",move=True,font=("",10))
        p._update()
    return palavra_secreta

def jogar():
    """ Função Principal de iteração do Jogo """

    caneta()
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    # Resetando as Variáveis 
    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)    

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print("PARABÉNS!! Você encontrou a palavra '{}'".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print('Faltam {} tentativas'.format(7-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")
    turtle.exitonclick()
        
if(__name__ == '__main__'):
    jogar()
