"""
    Questão OBI (Olimpíada Brasileira de Informática - 2007, Fase 1, Nível 1) - (Detectando Colisões)
    
    Detecção de colisão é uma das operações mais comuns (e importantes) em jogos eletrônicos. 
    O objetivo, basicamente, é verificar se dois objetos quaisquer colidiram, ou seja, se a interseção entre eles 
    não é vazia. Isso pode ser usado para saber se duas naves colidiram, se um monstro bateu em uma parede, 
    se um personagem pegou um item, etc. Para facilitar as coisas, muitas vezes os objetos são aproximados por 
    figuras geométricas simples (esferas, paralelepípedos, triângulos etc). Neste problema, os objetos são 
    aproximados por retângulos em um plano 2D.

    Escreva uma função chamada colisao que, dados dois retângulos, determine se eles se interceptam ou não. 
    
    Cada retângulo é determinado pelas coordenadas x e y de dois de seus vértices diametralmente opostos, 
    representando a diagonal que vai da esquerda para a direita e de baixo para cima. Os lados de cada retângulo 
    são sempre paralelos aos eixos x e y.
    
    Entrada: Os parâmetros de entrada são duas tuplas com quatro valores inteiros cada uma, representando as 
    coordenadas do primeiro retângulo e as coordenadas do segundo retângulo.
    
    Saída: Sua função deve retornar o valor booleano True caso haja interseção ou False caso não haja.
        Exemplos:
        Entrada: (0,0,1,1), (0,0,1,1) ; Saída: True
            ==> p1(0,0) ; p2(0,1) ; p3(1,1) ; p4(1,0)
        Entrada: (0,0,2,2), (1,1,3,3) ; Saída: True
            ==> p1(0,0) ; p2(0,2) ; p3(2,2) ; p4(2,0)
            ==> p5(1,1) ; p6(1,3) ; p7(3,3) ; p8(3,1)
        Entrada: (0,0,1,1), (2,2,3,3) ; Saída: False"    

Exemplo internet:
var rect1 = {x: 5, y: 5, width: 50, height: 50}
var rect2 = {x: 20, y: 10, width: 10, height: 10}

    if (rect1.x < rect2.x + rect2.width &&
    rect1.x + rect1.width > rect2.x &&
    rect1.y < rect2.y + rect2.height &&
    rect1.y + rect1.height > rect2.y) {
        // collision detected!
    }
    
    if ( (x1 < (x2 +l2) ) && ( (x1 +l1) > x2) && (y1 < (y2 + a2) && ( (y1 +a1) > y2) )
"""

def colisao(t1, t2):
    
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
t1 = (0,0,2,2)
t2 = (1,1,3,3)

result = colisao(t1, t2)
print(result)