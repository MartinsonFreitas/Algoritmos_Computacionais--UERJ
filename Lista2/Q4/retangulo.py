#Autor: Martinson Lima de Freitas

# importa a classe pai do Objeto Geométrico
from objetoGeometrico import Objeto_Geometrico

class Retangulo(Objeto_Geometrico):
    def __init__(self, base, altura, raio):
        super().__init__(base, altura, raio)
        
    def calcular_area(self):
        """ Calcula área da figura

        Returns:
            _type_: calcula a´rea da figura
        """
        return self.base * self.altura

    def calcular_perimetro(self):             
        """ Calcula o perímetro da figura

        Returns:
            _type_: calcula perímetro da figura
        """
        return 2 * self.base + 2 * self.altura