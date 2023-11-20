class Elevador:
    def __init__(self, capacidade, andares,):
        self.capacidade = capacidade
        self.andares = andares
        self.andar_atual = 0
        self.pessoas_presentes = 0
        
    def entrar(self):
        """Acrescenta uma pessoa no elevador se houver espaço
        """
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
        else:
            print('\n*** Não há espaço no elevador ***\n')
            
    def sair(self):
        """Acrescenta uma pessoa no elevador se houver espaço
        """
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
        else:
            print('\n*** Não há pessoas no elevador ***\n')
    
    def subir(self):
        """Acrescenta uma pessoa no elevador se houver espaço
        """
        if self.andar_atual < self.andares:
            self.andar_atual += 1
        else:
            print('\n*** Não há pessoas no elevador ***\n')
    
    def imprime(self):
        print('--------- Dados Elevador ---------')
        print('Capacidade:', self.capacidade)
        print('Total andares:', self.andares)
        print('Andar atual:', self.andar_atual)
        print('Pessoas presentes:', self.pessoas_presentes)


#principal
def main():
    elevador1 = Elevador(5,10)
    elevador1.imprime()
    
    for i in range(6):
        elevador1.entrar()
    elevador1.imprime()
    

# Teste
if __name__ == '__main__':
    main()