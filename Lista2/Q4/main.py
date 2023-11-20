#Autor: Martinson Lima de Freitas

import retangulo, caixa, circulo, cilindro

if __name__ == "__main__":
    retangulo = retangulo.Retangulo(5, 3, 0)
    caixa = caixa.Caixa(4, 6, 2)
    circulo = circulo.Circulo(0, 0, 3)
    cilindro = cilindro.Cilindro(0, 4, 8)

    print("Retângulo:")
    print("Área:", retangulo.calcular_area())
    print("Perímetro:", retangulo.calcular_perimetro())

    print("\nCaixa:")
    print("Área:", caixa.calcular_area())
    print("Volume:", caixa.calcular_volume())

    print("\nCírculo:")
    print("Área:", circulo.calcular_area())
    print("Perímetro:", circulo.calcular_perimetro())

    print("\nCilindro:")
    print("Área:", cilindro.calcular_area())
    print("Volume:", cilindro.calcular_volume())
