class Veiculo:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        
class Dispositivo:
    def __init__(self):
        self._voltagem = 220
        
class Carro(Veiculo, Dispositivo):
    def __init__(self, cor, modelo, ano):
        Veiculo.__init__(self, cor, modelo)
        Dispositivo.__init__(self)
        self.ano = ano
        