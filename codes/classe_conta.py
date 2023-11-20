class Conta:
    """Classe conta recebe cliente, numero de conta e saldo da Classe Cliente
    """
    def __init__(self, cliente, numero, saldo = 0): # Construtor da Classe conta
        """Instancia a classe

        Args:
            cliente (str): Nome do cliente
            numero (int): Número da conta do cliente
            saldo (float, optional): Saldo da conta do cliente. Defaults to 0.
        """
        self.saldo = 0
        self.cliente = cliente
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def saque(self, valor):
        """Registra as operações de saque na conta cliente

        Args:
            valor (float): Valor do saque a registrar.
        """
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])

    def deposito(self, valor):
        """Registra as operações de depósito na conta cliente

        Args:
            valor (float): Valor do saque a registrar.
        """
        self.saldo += valor
        self.operacoes.append(["Deposito", valor])

    def extrato(self):
        """Exibe as operações de saque e depósito da conta cliente
        """
        self.cliente.imprime()
        print("Extrato Conta N° %s\n" % self.numero)
        
        for op in self.operacoes:
            print("%10s %10.2f" % (op[0], op[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)

class Cliente:
    """Classe cliente
    """
    def __init__(self, nome, telefone):
        """Registra as informações de nome e telefone Cliente

        Args:
            nome (str): Nome do Cliente.
            telefone (str): Telefone do cliente.
        """
        self.nome = nome
        self.telefone = telefone

    def imprime(self):
        print('------ Dados do Cliente -------')
        print('Nome:', self.nome)
        print('Telefone:', self.telefone)

class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo = 0, limite = 0):
        Conta.__init__(self, cliente, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])

#teste
maria = Cliente("Maria da Silva", "(21)99654-3210")
conta2 = ContaEspecial(maria, 2, 500, 1000)
conta2.deposito(300)
conta2.saque(1500)
conta2.extrato()

#Principal
#popular a classe cliente
cliente1 = Cliente('Martinson Lima de Freitas', '21 99299-5201')
#print('Nome:', cliente1.nome)

c1 = Conta(cliente1, '123456')
c1.deposito(500)
c1.saque(200)
c1.extrato()
#print('Conta:', c1.numero)
#print('Saldo conta:', c1.saldo)
#print('Operações')
#print(c1.operacoes)