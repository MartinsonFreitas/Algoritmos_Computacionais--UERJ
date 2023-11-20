# Autor: Martinson Lima de Freitas

import math

class Ponto2D:
    """ 
        Classe Ponto2D que represente um ponto no plano cartesiano.
    """
    
    def __init__(self, x=0, y=0):
        """ Inicia o construto da classe:
        
        i. Por default (sem parâmetros) na origem do espaço 2D;
        ii. Num local indicado por dois parâmetros (indicando o valor de abcissa e ordenada do ponto 
        que está sendo criado);

        Args:
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
        """
        self.x = x
        self.y = y

    def calcular_distancia(self, ponto):
        """ Calcula a distância entre dois pontos usando a equação de Euclides

        Args:
            ponto (_x, y_): Dois pontos no Plano cartesiano

        Returns:
            _Float_: Retorna o valor da distância calculada.
        """
        dx = ponto.x - self.x
        dy = ponto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        
        return distancia