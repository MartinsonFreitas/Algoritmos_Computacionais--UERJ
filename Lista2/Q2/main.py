# Autor: Martinson Lima de Freitas

import trianguloClass

# Função main para testar a classe
def main():
    try:
        triangulo = trianguloClass.Triangulo(5, 5, 5)
        print("Tipo do triângulo:", triangulo.tipoTriangulo())
        print("Perímetro:", triangulo.calculaPerimetro())
        print("Área:", triangulo.calculaArea())
    except ValueError as e:
        print("Erro:", str(e))

if __name__ == "__main__":
    main()
