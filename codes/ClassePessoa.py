class Pessoa():
    '''Recebe os dados de uma pessoa'''
    
    def __init__(self, cpf, nome, telefone) -> None: # Construtor da Classe Pessoa
        """Instancia a Classe Pessoa

        Args:
            cpf (_str_): Recebe o CPF de Pessoa
            nome (_str_): Recebe o nome de Pessoa
            telefone (_str_): Recebe o telefone de Pessoa
        """
        
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        
    def respirar(self, nome):
        print( nome, 'Respirando...')
        
        
class Aluno(Pessoa):
    def __init__(self, cpf, nome, telefone, matricula, cr):
        Pessoa.__init__(self, cpf, nome, telefone)
        self.matricula = matricula
        self.cr = cr

    def assistirAula(self, nome):
        print(nome, 'Assistindo aula...')
        
class Professor(Pessoa):
    def __init__(self, cpf, nome, telefone, salario):
        Pessoa.__init__(self, cpf, nome, telefone)
        self.salario = salario

    def darAula(self):
        print('Dando aula...')
        
class Coordenador(Professor):
    def __init__(self, cpf, nome, telefone, salario):
        Professor.__init__(self, cpf, nome, telefone)
        
    def coordenar(self):
        print('Coordenado...')
        
#teste
if __name__ == '__main__':
    p = Pessoa('12345678901', 'João da Silva', '(21)987-654321')
    p.respirar(p.nome)
    a = Aluno('12345678901', 'Ana Claudia', '(21)9123-45678','1234', 7)
    a.respirar(a.nome)
    a.assistirAula(a.nome)
    # crie objetos da classe professor e coordenador...