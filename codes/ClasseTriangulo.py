"""
Q2. Crie uma classe chamada Triangulo contendo os três lados como atributos (a, b e c) e os seguintes métodos:
a) Método construtor para inicializar o triângulo, desde que seja válido. Obs. Use o método do item b.
b) Método ehValido que retorna verdadeiro se o triângulo é válido (o lado maior deve ser menor que a 
soma dos outros lados), senão retorna falso.
c) Método tipoTriangulo que retorna o tipo do triângulo. Se possuir os 3 lados iguais, é equilátero. 
Se possuir apenas 2 lados iguais, é isósceles e se possuir os 3 lados com valores diferentes é escaleno.
d) Método calculaPerimetro que retorna o perímetro do triângulo.
e) Método calculaArea que retorna a área do triângulo. A área do triângulo pode ser aproximada pela 
fórmula de Heron, conforme a Equação abaixo, onde a, b e c são os lados do triângulo e p é o seu semiperímetro 
(perímetro/2).
𝐴𝑟𝑒𝑎=√𝑝×(𝑝−𝑎)×(𝑝−𝑏)×(𝑝−𝑐)
f) Crie uma função main (fora da definição da classe) para testar a sua classe com os diferentes métodos e 
situações:
"""

class Triangulo(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validarForma(self):
        pass


# Caso positivo
triangulo = Triangulo(3, 4, 5)
assert triangulo.validarForma()

# Caso negativo
triangulo = Triangulo(1, 4, 5)
assert not triangulo.validarForma()


def validarForma(self):
    if (self.a < (self.b + self.c)):
        if (self.b < (self.a + self.c)):
            if (self.c < (self.a + self.b)):
                return True

    return False