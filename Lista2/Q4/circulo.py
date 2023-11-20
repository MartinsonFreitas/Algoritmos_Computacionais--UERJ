#Autor: Martinson Lima de Freitas

import math

# importa a classe pai do Objeto Geométrico
from objetoGeometrico import Objeto_Geometrico

class Circulo(Objeto_Geometrico):
    def calcular_area(self):
        """ Calcula área da figura

        Returns:
            _type_: calcula a´rea da figura
        """
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):             
        """ Calcula o perímetro da figura

        Returns:
            _type_: calcula perímetro da figura
        """
        return 2 * math.pi * self.raio

