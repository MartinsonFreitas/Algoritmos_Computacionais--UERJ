import turtle as t

def desenha(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for y in range(n):
        for x in range(n):
            t.goto(15*x, 15*y)
            t.dot()
            
    t.done()
        
def desenha_v2(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for x in range(n):
        for y in range(n):
            t.goto(15*x, 15*y)
            t.dot()
    
    t.done()
        
def desenha_v3(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for x in range(n):
        for y in range(x):
            t.goto(15*x, 15*y)
            t.dot()
    
    t.done()
        
def desenha_v4(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for x in range(n):
        for y in range(n-x):
            t.goto(15*x, 15*y)
            t.dot()
    
    t.done()
    
def desenha_v5(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for x in range(n):
        for y in range(n):
            if x < y:
                t.color('red')
            else:
                t.color('blue')
                
            t.goto(15*x, 15*y)
            t.dot()
    
    t.done()
    
from random import randint
def desenha_v6(n):
    #t.speed('fastest')
    t.hideturtle()
    t.up()
    
    for x in range(n):
        valor = randint(0,n)
        for y in range(valor):
            if x < y:
                t.color('red')
            else:
                t.color('blue')
                
            t.goto(15*x, 15*y)
            t.dot()
    
    t.done()
        
#principal
desenha_v6(10)