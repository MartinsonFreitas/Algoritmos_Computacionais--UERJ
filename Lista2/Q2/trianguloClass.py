# Autor: Martinson Lima de Freitas

import math

class Triangulo:
    """ Classe de validação de triângulos
    """
    
    def __init__(self, a, b, c):
        """ inicializa a construção da classe

        Args:
            a (_Int_): Recebe o valor do lado a do triângulo
            b (_Int_): Recebe o valor do lado b do triângulo
            c (_Int_): Recebe o valor do lado c do triângulo

        Raises:
            ValueError: _description_
        """
        if self.ehValido(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Os lados fornecidos não formam um triângulo válido.")

    def ehValido(self, a, b, c):
        """ Valida o triângulo, se a soma dos lados for maior que o lado oposto, não valida o triângulo """
        return a + b > c and a + c > b and b + c > a

    def tipoTriangulo(self):
        """ Classifica o triângulo de acordo com os lados

        Returns:
            _String_: Retorna a classificação do triângulo
        """
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"

    def calculaPerimetro(self):
        """ Calcula o perímetro somando os lados do triângulo

        Returns:
            _Int_: Valor do Perímetro do triângulo.
        """
        return self.a + self.b + self.c

    def calculaArea(self):
        """ Calcula área do triângulo utilizando a fórmula de Heron

        Returns:
            _Float_: Valor da área do triângulo.
        """
        p = self.calculaPerimetro() / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area