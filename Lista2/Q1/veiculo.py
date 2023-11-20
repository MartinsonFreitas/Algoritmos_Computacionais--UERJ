# Autor: Martinson Lima de Freitas

class Veiculo:
    """
        Cria a Classe Veículo, onde consumo é a razão combustível/Km rodado, e 'capacidade' 
        de combustível que cabe no tanque de gasolina.
    """
    def __init__(self, consumo, capacidade):
        """ Construtor da Classe Veículo

        Args:
            consumo (_Int_): Consumo de combustível por kilometro rodado.
            capacidade (_Int_): Capacidade máxima de combustível no tanque de gasolina.
        """
        self.consumo = consumo
        self.capacidade = capacidade
        self.combustivel = 0

    def mover(self, distancia):
        """ Move o veículo

        Args:
            distancia (_Int_): Distância percorrida se tiver combustível no veículo.
        """
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"Veículo se moveu {distancia} km.")
        else:
            print("Sem combustível suficiente para percorrer a distância desejada.")

    def getCombustivel(self):
        """ Abastece veículo.

        Returns:
            _Int_: Quantidade de combustível no abastecimento, não pode exceder a capacidade do tanque.
        """
        return self.combustivel

    def abastecer(self, quantidade):
        """Abastece veículo, se couber no tanque, abastece, se não, retorna mensagem...

        Args:
            quantidade (_Int_): Quantidade de combustível.
        """
        espaco_disponivel = self.capacidade - self.combustivel
        if quantidade <= espaco_disponivel:
            self.combustivel += quantidade
            print(f"Veículo abastecido com {quantidade} litros de combustível.")
        else:
            print("Capacidade máxima do tanque excedida. Abastecido apenas até a capacidade máxima.")