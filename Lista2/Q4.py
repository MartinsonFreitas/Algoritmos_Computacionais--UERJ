"""
Q4. Considere os seguintes objetos geométricos: retângulo, caixa, círculo e cilindro. 
Cada objeto geométrico deve possuir métodos para obter seu perímetro (figuras 2D), sua área (
    externa, no caso das 3D) e volume (figuras 3D). Crie um diagrama de classes que modele objetos 
    geométricos de forma a aproveitar ao máximo suas características comuns. Depois implemente em python o 
    modelo criado. As classes devem possuir construtores parametrizados, os quais devem ser utilizados para 
    inicialização dos atributos dos objetos. Considere as informações abaixo para o cálculo do perímetro, 
    área e volume dos objetos. Finalmente crie um programa de teste que instancie objetos das classes e 
    invoque as funcionalidades implementadas.
• Retângulo:
• Área = base*altura,
• Perímetro = 2*base + 2*altura
• Caixa:
• Volume = base1*base2*altura,
• Área = 2*(base1*base2 + base1*altura + base2*altura)
• Círculo:
• Área = 3.14*(raio)2,
• Perímetro = 2*3.14*raio
• Cilindro:
• Volume = 3.14*(raio)2*altura,
• Área = 2*3.14*(raio)2 + 2*3.14*raio*altura


+----------------------+
|    ObjetoGeometrico  |
+----------------------+
|                      |
| - base               |
| - altura             |
| - raio               |
|                      |
| + calcular_area()    |
| + calcular_perimetro() |
| + calcular_volume()  |
+----------------------+
          ^
          |
          |
+------------------------+
|       Retangulo        |
+------------------------+
|                        |
| + calcular_area()      |
| + calcular_perimetro() |
+------------------------+
          ^
          |
          |
+------------------------+
|         Caixa          |
+------------------------+
|                        |
| + calcular_area()      |
| + calcular_volume()    |
+------------------------+
          ^
          |
          |
+------------------------+
|        Circulo         |
+------------------------+
|                        |
| + calcular_area()      |
| + calcular_perimetro() |
+------------------------+
          ^
          |
          |
+------------------------+
|        Cilindro         |
+------------------------+
|                        |
| + calcular_area()      |
| + calcular_volume()    |
+------------------------+

"""

import math

class ObjetoGeometrico:
    def __init__(self, base, altura, raio):
        self.base = base
        self.altura = altura
        self.raio = raio

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def calcular_volume(self):
        pass

class Retangulo(ObjetoGeometrico):
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class Caixa(ObjetoGeometrico):
    def calcular_area(self):
        return 2 * (self.base * self.altura + self.base * self.raio + self.altura * self.raio)

    def calcular_volume(self):
        return self.base * self.altura * self.raio

class Circulo(ObjetoGeometrico):
    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Cilindro(ObjetoGeometrico):
    def calcular_area(self):
        return 2 * math.pi * (self.raio ** 2) + 2 * math.pi * self.raio * self.altura

    def calcular_volume(self):
        return math.pi * (self.raio ** 2) * self.altura
    
retangulo = Retangulo(5, 3, 0)
caixa = Caixa(4, 6, 2)
circulo = Circulo(0, 0, 3)
cilindro = Cilindro(0, 4, 8)

print("Retângulo:")
print("Área:", retangulo.calcular_area())
print("Perímetro:", retangulo.calcular_perimetro())

print("\nCaixa:")
print("Área:", caixa.calcular_area())
print("Volume:", caixa.calcular_volume())

print("\nCírculo:")
print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

print("\nCilindro:")
print("Área:", cilindro.calcular_area())
print("Volume:", cilindro.calcular_volume())
