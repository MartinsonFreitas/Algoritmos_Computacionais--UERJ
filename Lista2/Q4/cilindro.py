#Autor: Martinson Lima de Freitas

import math

# importa a classe pai do Objeto Geométrico
from objetoGeometrico import Objeto_Geometrico

class Cilindro(Objeto_Geometrico):
    def calcular_area(self):        
        """ Calcula área da figura

        Returns:
            _type_: calcula a´rea da figura
        """
        return 2 * math.pi * (self.raio ** 2) + 2 * math.pi * self.raio * self.altura

    def calcular_volume(self):     
        """ Calcula o volume da figura

        Returns:
            _type_: calcula volume da figura
        """
        return math.pi * (self.raio ** 2) * self.altura