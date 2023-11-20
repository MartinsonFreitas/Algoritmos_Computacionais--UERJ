class Conta:
    def __initi__(self, cliente, saldo):
        self.__cliente = cliente
        self.__saldo = saldo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, valor):
        self.__saldo += valor
        
    def __str__(self) -> str:
        return 'Cliente: ' +self.cliente + ', Saldo: '+str(self.saldo)
    
    
    #teste
    