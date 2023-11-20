#Autor: Martinson Lima de Freitas

# importa a classe pai do Objeto Geométrico
from objetoGeometrico import Objeto_Geometrico

class Caixa(Objeto_Geometrico):
    """ Classe Caixa

    Args:
        Objeto_Geometrico (_base, altura, raio_): Medidas da figura geométrica
    """
    def calcular_area(self):
        """ Calcula área da figura

        Returns:
            _type_: calcula a´rea da figura
        """
        return 2 * (self.base * self.altura + self.base * self.raio + self.altura * self.raio)

    def calcular_volume(self):        
        """ Calcula o volume da figura

        Returns:
            _type_: calcula volume da figura
        """
        return self.base * self.altura * self.raio
    