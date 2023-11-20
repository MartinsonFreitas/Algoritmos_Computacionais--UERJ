class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        print("\nGet raio")
        return self.__raio

    @raio.setter
    def raio(self, value):
        print("\nSet raio")
        self.__raio= value

    @raio.deleter    
    def raio(self):
        print("\nDelete raio")
        del self.__raio

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def area(self):
        return self.ladoA * self.ladoB

    def perimetro(self):
        return 2*self.ladoA + 2*self.ladoB

class Quadrado(Retangulo):
    def __init__(self, lado):
        super(Quadrado, self).__init__(lado, lado)

#teste
"""circ = Circulo(20)
print(circ.raio)

circ.raio = 100.0
print(circ.raio)

del circ.raio
print(circ.raio)"""

r = Retangulo(2,3)
print("Área do retângulo:", r.area())
print("Perímentro do retângulo:", r.perimetro(), '\n')

c = Quadrado(5)
print("Área do quadrado:", c.area())
print("Perímetro do quadrado:", c.perimetro(), '\n')