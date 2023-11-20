# Autor: Martinson Lima de Freitas

import veiculo

# Função main para testar a classe
def main():
    veiculo = veiculo.Veiculo(10, 50)  # Consumo de 10 km/litro e capacidade do tanque de 50 litros

    veiculo.abastecer(30)  # Abastece o veículo com 30 litros
    print("Combustível:", veiculo.getCombustivel())

    veiculo.mover(200)  # Move o veículo por 200 km
    print("Combustível:", veiculo.getCombustivel())

    veiculo.mover(100)  # Tenta mover o veículo por mais 100 km, mas não há combustível suficiente
    print("Combustível:", veiculo.getCombustivel())

    veiculo.abastecer(40)  # Tenta abastecer o veículo com 40 litros, mas excede a capacidade máxima
    print("Combustível:", veiculo.getCombustivel())

if __name__ == "__main__":
    main()