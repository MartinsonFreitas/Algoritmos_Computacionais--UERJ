"""
Q1. Crie uma classe Veiculo com as seguintes características:

a) Um veículo tem um certo consumo de combustível (medido em km/litro), 
uma certa quantidade de combustível no tanque e uma capacidade máxima de combustível.

b) O consumo e a capacidade do tanque são especificados no construtor da classe.

c) Crie um método mover que receba a distância em quilômetros e reduz o nível de combustível no 
tanque baseado no consumo do veículo. Não permitir que o veículo se mova se estiver sem combustível.

d) Crie um método getCombustivel(), que retorne o nível atual de combustível.

e) Crie um método abastecer, para abastecer o tanque (sem ultrapassar a capacidade máxima do tanque).

f) Crie uma função main (fora da definição da classe) para testar a sua classe com os diferentes métodos e 
situações: Crie um veículo, abastece o tanque, ande, mande mostrar a quantidade de combustível e teste as 
validações que você criou para não permitir situações impossíveis    
"""
class Veiculo:

    def __init__(self, consumo, kilometragem, capacidade):
        self.__consumo = consumo                        # km/litro
        self.__kilometragem = kilometragem              # Kilometregem do carro
        self.__capacidade = capacidade                  # capacidade de combustível no tanque
        self.__combustivel = 0                          # carro  inicia sem combustível

    def __verifica_tanque(self, valor):
        if ((self.__combustivel + valor) <= self.__capacidade): # verifica a capacidade de combustível
            return valor
        else:   #se não estiver cheio, completa o tanque
            return (self.__capacidade - self.__combustivel) #retorna a capacidade do tanque

    def abastecer(self, volume):   # abastecer o carro
        abastecer = self.__verifica_tanque(volume)
        self.__combustivel += abastecer
        print("Tanque abastecido com {} litros de combustível. Seu tanque agora tem {} litros".format(abastecer, self.__combustivel_no_tanque))

    def __pode_andar(self, kilometragem):  # verifica se tem combustível para rodar os Kms
        consumo = (kilometragem / self.__consumo) # litros que serão gastos na corrida
        return (self.__capacidade >= consumo)

    def andar(self, km): #Roda os km e adiciona os Kms do carro / reduz o combustível
        if (self.__pode_andar(km)):
            self.__kilometragem += km
            self.__combustivel -= (km / self.__consumo)
        else:
            print("Combustível insuficiente para andar {}Km".format(km))

    def tanque(self): #imprime a quantidade de litros que tem no carro
        print("Restam {} litros no tanque de combustível".format(self.__combustivel))

    #propriedades da Classe Carro
    @property
    def consumo(self):
        return self.__consumo

    @property
    def capacidade_tanque(self):
        return self.__capacidade

    @property
    def kilometragem(self):
        return self.__kilometragem

    @property
    def combustiven_no_tanque(self):
        return self.__combustivel

#teste
