class Tempo:
    '''Classe tempo com propriedades de leitura/escrita'''
    def __init__(self, hora=0, minuto=0, segundo=0):
        '''Inicializa cada atributo'''
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
        
    @property
    def hora(self):
        '''Retorna o atributo hora'''
        return self.__hora

    @hora.setter
    def hora(self, hora):
        '''Modifica o atributo hora'''
        if not(0 <= hora < 24):
            print(f'Hora ({hora}) deve estar entre 0-23')
        else:
            self.__hora = hora
            
    @property
    def minuto(self):
        '''Retorna o atributo minuto'''
        return self.__minuto

    @minuto.setter
    def minuto(self, minuto):
        '''Modifica o atributo hora'''
        if not(0 <= minuto < 60):
            print(f'Minuto ({minuto}) deve estar entre 0-59')
        else:
            self.__minuto = minuto
            
    @property
    def segundo(self):
        '''Retorna o atributo segundo'''
        return self.__segundo

    @segundo.setter
    def segundo(self, segundo):
        '''Modifica o atributo segundo'''
        if not(0 <= segundo < 60):
            print(f'Segundo ({segundo}) deve estar entre 0-59')
        else:
            self.__segundo = segundo
            
    def __str__(self):
        '''método especial para retornar uma representação de
        string de um objeto.'''
        return '%.2d:%.2d:%.2d' % (self.hora, self.minuto, self.segundo)
    
#teste
if __name__ == '__main__':
    # Criamos um objeto t1
    t1 = Tempo()
    print('Tempo 1:',t1)
    t1.hora = 13
    t1.minuto = 25
    t1.segundo = 42
    print('Tempo 1 atualizado:',t1)

    # Criamos um objeto t2
    t2 = Tempo(9,40,14)
    print('Tempo 2:',t2)