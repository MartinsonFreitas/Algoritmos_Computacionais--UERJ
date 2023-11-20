ficha = {'nome':'Carlos', 'profissão': 'Engenheiro', 'Salário': 7000, 'Idade': 34}
notas_aluno = {'Matemática': 8.5, 'Ciências': 7.2, 'História': 6.8}

def listar_dicionario(ficha):
    for tupla in ficha.items():
        print(tupla[0],':',tupla[1])
    

def calc_media(notas_aluno):
    """Retorna a média das notas de um aluno
    dict -> float

    Args:
        notas_aluno (Dicionário): Dados fornecidos num dicionário de dados
    """
    soma = 0
    for nota in notas_aluno.values():
        soma+= nota
        
    return soma/len(notas_aluno)

def maior_nota(notas_aluno):
    """Retorna a maior nota de um aluno
    dict -> float

    Args:
        notas_aluno (Dicionário): Dados fornecidos num dicionário de dados
    """
    maior_nota = 0
    materia=''
    for disciplina in notas_aluno.keys():
        if notas_aluno[disciplina] > maior_nota:
            maior_nota = notas_aluno[disciplina]
            materia = disciplina
                    
    return materia, maior_nota

media = calc_media(notas_aluno)
maior = maior_nota(notas_aluno)
print('A maior nota é:', maior)