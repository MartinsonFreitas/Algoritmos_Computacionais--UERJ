#Autor: Martinson Lima de Freitas

class Objeto_Geometrico:
    """ Construtor da Classe Pai --> Objeto Geométrico
    """
    def __init__(self, base, altura, raio):
        """ Define os parâmetros básicos das figuras geométricas

        Args:
            base (_float / int_): Recebe as medidas da base da figura geométrica.
            altura (_float / int_): Recebe as medidas da altura da figura geométrica.
            raio (_float / int_): Recebe as medidas do raio da figura geométrica.
        """
        self.base = base
        self.altura = altura
        self.raio = raio

    def calcular_area(self):
        """
            método a ser implementado pela classe filha
        """
        pass

    def calcular_perimetro(self):
        """
            método a ser implementado pela classe filha
        """
        pass

    def calcular_volume(self):
        """
            método a ser implementado pela classe filha
        """
        pass
