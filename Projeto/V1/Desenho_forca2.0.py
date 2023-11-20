import turtle

palavra ='paralelepiledo' #palavra secreta

wn = turtle.Screen() #configurações de tela
turtle.title('Forca')# titulo do grafico
wn.bgcolor("lightyellow") #cor de fundo


t=turtle.Turtle() #t é o cursor do desenho da forca
turtle.title('Forca')

 
def desenho_da_forca():
    '''função que cria o desenho da forca basica'''

    #base retangular inicial:inicio(0,0) fim (0,0) 200*50
    t.pen( fillcolor="brown", pensize=3, speed=9)  #alterar a velocidade no final)
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

    #corda (150,-15): (150,-40)
    t.goto(150,-17)
    t.pen(pencolor='brown',pensize=2)
    t.down()
    t.lt(90)
    t.fd(25)
    t.rt(90)
    t.circle(20)
    t.lt(90)
    t.pen(pencolor='black')
    t.up()
    t.goto(30,-200)
    t.lt(90)
    

    #espacos das letras
    for lacunas in range(len(palavra)):
        t.down()
        t.fd(10)
        t.up()
        t.fd(5)
        

def desenho_da_pessoa(erros):
    '''função que desenha o corpo da pessao enforcada membro a membro
de acordo com a quantidade de erros)'''

    if erros==1:
        #cabeça (150,-40) (150,-40 + 2r )
        t.up()
        t.pen(pencolor="brown", fillcolor="pink", pensize=2)
        t.goto(150,-40)
        t.begin_fill()
        t.rt(180)
        t.down()
        t.circle(20)
        t.up()
        t.end_fill()

    elif erros==2:
        #corpo palito
        t.goto(150,-87)
        t.color("pink")
        t.down()
        t.pensize(15)
        t.lt(90)
        t.fd(45)
        t.up()

    elif erros==3:
        #braço esquerdo palito
        t.goto(150,-87)
        t.down()
        t.pensize(10)
        t.lt(40)
        t.fd(35)
        t.up()
        
    elif erros==4:
        #braço direito palito
        t.goto(150,-87)
        t.down()
        t.pensize(10)
        t.rt(80)
        t.fd(35)
        t.up()
        
    elif erros==5:
        #perna esquerda palito
        t.goto(150,-130)
        t.down()
        t.pensize(10)
        t.fd(35)
        t.up()
        
    elif erros==6:
        #perna direita palito
        t.goto(150,-130)
        t.down()
        t.pensize(10)
        t.setheading(-45)
        t.fd(35)
        t.up()

    elif erros==7:
        #morte
        #cabeça (150,-40) (150,-40 + 2r )
        t.up()
        t.color("purple")
        t.setheading(180)
        t.pensize(2)
        t.goto(150,-40)
        t.begin_fill()
        t.down()
        t.circle(20)
        t.up()
        t.end_fill()

        # x no olho direito
        t.goto(160,-50)
        t.color("white")
        t.down()
        t.lt(45)
        t.fd(10)
        t.up()
        
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
        
        


#test
desenho_da_forca()
desenho_da_pessoa(1)
desenho_da_pessoa(2)
desenho_da_pessoa(3)
desenho_da_pessoa(4)
desenho_da_pessoa(5)
desenho_da_pessoa(6)
desenho_da_pessoa(7)
