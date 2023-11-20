# Autor: Martinson Lima de Freitas

import ponto2D

# Função main para testar a classe
def main():
    # Testando o construtor padrão (origem)
    ponto1 = ponto2D.Ponto2D()
    print("Ponto 1:", ponto1.x, ponto1.y)

    # Testando o construtor com parâmetros (3, 4)
    ponto2 = ponto2D.Ponto2D(3, 4)
    print("Ponto 2:", ponto2.x, ponto2.y)

    # Calculando a distância entre os pontos 1 e 2
    distancia = ponto1.calcular_distancia(ponto2)
    print("Distância entre ponto 1 e ponto 2:", distancia)

if __name__ == "__main__":
    main()
