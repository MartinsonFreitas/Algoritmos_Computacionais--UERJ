class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        
    def area(self):
        return self.ladoA * self.ladoB
    
    def perimetro(self):
        return 2*self.ladoA + 2*self.ladoB
    
    
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4*self.lado