>>> L = [1,2,3,4,5]
>>> type(L)
<class 'list'>
>>> L[0]
1
>>> L[-2]
4
>>> L[0] = 8
>>> L
[8, 2, 3, 4, 5]
>>> L[-2] = 'OLÁ'
>>> L
[8, 2, 3, 'OLÁ', 5]
>>> L[2] = 2.5
>>> L[-1]=(8,True)
>>> L
[8, 2, 2.5, 'OLÁ', (8, True)]
>>> L[0]=L[1]=3
>>> L
[3, 3, 2.5, 'OLÁ', (8, True)]
>>> L[0,3]=9
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    L[0,3]=9
TypeError: list indices must be integers or slices, not tuple
>>> L[0:2]=12
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    L[0:2]=12
TypeError: can only assign an iterable
>>> L
[3, 3, 2.5, 'OLÁ', (8, True)]
>>> L[0:1]=12
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    L[0:1]=12
TypeError: can only assign an iterable
>>> L[0:1]=[12]
>>> L
[12, 3, 2.5, 'OLÁ', (8, True)]
>>> L + [1,2]
[12, 3, 2.5, 'OLÁ', (8, True), 1, 2]
>>> L
[12, 3, 2.5, 'OLÁ', (8, True)]
>>> L +(1,2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    L +(1,2)
TypeError: can only concatenate list (not "tuple") to list
>>> L
[12, 3, 2.5, 'OLÁ', (8, True)]
>>> L*2
[12, 3, 2.5, 'OLÁ', (8, True), 12, 3, 2.5, 'OLÁ', (8, True)]
>>> L*0
[]
>>> t = 1,2,3
>>> t
(1, 2, 3)
>>> t[0] = 5
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t[0] = 5
TypeError: 'tuple' object does not support item assignment
>>> L = [1,2,3]
>>> L[0]=5
>>> L
[5, 2, 3]
>>> L
[5, 2, 3]
>>> L = [12, 3, 2.5, 'OLÁ', (8, True)]
>>> 3 in L
True
>>> 'olá' in L
False
>>> 'OLÁ' in L
True
>>> 8 in L
False
>>> L[-1]
(8, True)
>>> L[-1][0]
8
>>> p1 = ('João da Silva', 28, 2500.00)
>>> p1 = ('Maria Eduarda', 32, 2800.00)
>>> p1 = ('João da Silva', 28, 2500.00)
>>> p2 = ('Maria Eduarda', 32, 2800.00)
>>> p1
('João da Silva', 28, 2500.0)
>>> p2
('Maria Eduarda', 32, 2800.0)
>>> L = [p1, p2]
>>> L
[('João da Silva', 28, 2500.0), ('Maria Eduarda', 32, 2800.0)]
>>> L = [L, L]
>>> L
[[('João da Silva', 28, 2500.0), ('Maria Eduarda', 32, 2800.0)], [('João da Silva', 28, 2500.0), ('Maria Eduarda', 32, 2800.0)]]
>>> p1
('João da Silva', 28, 2500.0)
>>> p1 = list(p1)
>>> p1
['João da Silva', 28, 2500.0]
>>> p2 = list(p2)
>>> p2
['Maria Eduarda', 32, 2800.0]
>>> L = [p1, p2]
>>> L
[['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0]]
>>> L[0][-1] = L[0][-1]*1.1
>>> L
[['João da Silva', 28, 2750.0], ['Maria Eduarda', 32, 2800.0]]
>>> 
= RESTART: C:/Users/Edhel/Desktop/UERJ/2023-I/Alg. comp/programas/listas/lista_pessoas.py
>>> L
[['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0], ['Enrique Caio', 50, 4100.0]]
>>> bonificar(L,'Maria Eduarda')
>>> L
[['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 3080.0000000000005], ['Enrique Caio', 50, 4100.0]]
>>> bonificar(L,'João')
Pessoa não existe
>>> bonificar(L,'João da Silva ')
Pessoa não existe
>>> bonificar(L,'João da silva')
Pessoa não existe
>>> 
= RESTART: C:/Users/Edhel/Desktop/UERJ/2023-I/Alg. comp/programas/listas/lista_pessoas.py
>>> bonificar(L,'João da silva')
>>> L
[['João da Silva', 28, 2750.0], ['Maria Eduarda', 32, 2800.0], ['Enrique Caio', 50, 4100.0]]
>>> 
= RESTART: C:/Users/Edhel/Desktop/UERJ/2023-I/Alg. comp/programas/listas/lista_pessoas.py
>>> L
[['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0], ['Enrique Caio', 50, 4100.0]]
>>> remover(L,'Enrique caio')
>>> L
[['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0]]
>>> remover(L,'JOÃO DA SILVA')
>>> L
[['Maria Eduarda', 32, 2800.0]]
>>> remover(L,'maria')
Pessoa não existe
>>> L
[['Maria Eduarda', 32, 2800.0]]
>>> L = [3,2,1,6]
>>> L.append(True)
>>> L
[3, 2, 1, 6, True]
>>> L.append('olá')
>>> L
[3, 2, 1, 6, True, 'olá']
>>> L.append((5,4))
>>> L
[3, 2, 1, 6, True, 'olá', (5, 4)]
>>> L.insert(1,9)
>>> L
[3, 9, 2, 1, 6, True, 'olá', (5, 4)]
>>> L.insert(-2,False)
>>> L
[3, 9, 2, 1, 6, True, False, 'olá', (5, 4)]
>>> L.insert(9,9)
>>> L
[3, 9, 2, 1, 6, True, False, 'olá', (5, 4), 9]
>>> L.insert(500,20)
>>> L
[3, 9, 2, 1, 6, True, False, 'olá', (5, 4), 9, 20]
>>> L.insert(-99,11)
>>> L
[11, 3, 9, 2, 1, 6, True, False, 'olá', (5, 4), 9, 20]
>>> 'Enrique' < 'João da Silva'
True
>>> 'Enrique' < 'Maria Eduarda'
True
>>> 'Enrique' < 'Enrique caio'
True
>>> 'Enrique' < 'enrique caio'
True
>>> 'enrique' < 'Enrique caio'
False
>>> 
= RESTART: C:/Users/Edhel/Desktop/UERJ/2023-I/Alg. comp/programas/listas/lista_pessoas.py
>>> inserir_ordenador(L, p)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    inserir_ordenador(L, p)
NameError: name 'p' is not defined
>>> inserir_ordenador(L, P)
>>> L
[['Enrique', 43, 3200.0], ['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0], ['Paulo Caio', 50, 4100.0]]
>>> P2 = ['Gabriel', 20, 1100.0]
>>> inserir_ordenador(L, P2)
>>> L
[['Enrique', 43, 3200.0], ['Gabriel', 20, 1100.0], ['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0], ['Paulo Caio', 50, 4100.0]]
>>> P3 = ['Xuxa', 62, 102800.0]
>>> inserir_ordenador(L, P3)
>>> L
[['Enrique', 43, 3200.0], ['Gabriel', 20, 1100.0], ['João da Silva', 28, 2500.0], ['Maria Eduarda', 32, 2800.0], ['Paulo Caio', 50, 4100.0], ['Xuxa', 62, 102800.0]]
>>> L = [5,2,6,9,4]
>>> L
[5, 2, 6, 9, 4]
>>> L[1:1]
[]
>>> L[1:1] = [8]
>>> L
[5, 8, 2, 6, 9, 4]
>>> L[3:3]='ola'
>>> L
[5, 8, 2, 'o', 'l', 'a', 6, 9, 4]
>>> L[3:3] = True
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    L[3:3] = True
TypeError: can only assign an iterable
>>> L[:1]= [8,9]
>>> L
[8, 9, 8, 2, 'o', 'l', 'a', 6, 9, 4]
>>> L[3:6]=[[5]]
>>> L
[8, 9, 8, [5], 'a', 6, 9, 4]
>>> L[5:5]=(1,2,3)
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4]
>>> L.extend([99,88])
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4, 99, 88]
>>> L.extend('computação')
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4, 99, 88, 'c', 'o', 'm', 'p', 'u', 't', 'a', 'ç', 'ã', 'o']
>>> L.append('sistemas')
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4, 99, 88, 'c', 'o', 'm', 'p', 'u', 't', 'a', 'ç', 'ã', 'o', 'sistemas']
>>> L.extend(55)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    L.extend(55)
TypeError: 'int' object is not iterable
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4, 99, 88, 'c', 'o', 'm', 'p', 'u', 't', 'a', 'ç', 'ã', 'o', 'sistemas']
>>> L.pop()
'sistemas'
>>> L
[8, 9, 8, [5], 'a', 1, 2, 3, 6, 9, 4, 99, 88, 'c', 'o', 'm', 'p', 'u', 't', 'a', 'ç', 'ã', 'o']
>>> L.pop(5)
1
>>> L
[8, 9, 8, [5], 'a', 2, 3, 6, 9, 4, 99, 88, 'c', 'o', 'm', 'p', 'u', 't', 'a', 'ç', 'ã', 'o']
>>> 