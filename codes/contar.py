"""
    Escreva um programa que conte de 1 a 5.000.000, de 1 em 1. Toda vez que a contagem
    atingir um múltiplo de 1.000.000, imprima este número na tela. Use seu relógio para
    cronometrar quanto tempo leva cada milhão de repetições do loop.
"""

def contar(n):
    #i = 1
    for i in range (1, n+1):
        if i % 1000000 == 0:           
            print(i)
            
#main
contar(5000000)