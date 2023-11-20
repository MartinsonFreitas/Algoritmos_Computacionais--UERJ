def divisiveis(L, n):
    """Retorna os elmentos de L divisiveis por n
    list, int -> list
    """
    L2 = [] # Criamos uma lista vazia contendo os divisiveis
    #percorrer os elementos da lista L
    for elemento in L:
        if elemento % n == 0 :#elemento é divisivel por n
            L2.append(elemento) # adicionamos na lista

    return L2
