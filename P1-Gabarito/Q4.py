def remove_condicional(L,x):
    """Função que remove a primeira ocorrencia de x de uma lista
    quando aparace um número par de vezes
    list, int -> list
    """
    ocorrencias = L.count(x) #quantaas vezes x está em L
    if ocorrencias % 2 == 0: #par
        L.remove(x)

    return L


def numero_ocorrencias(L,x):
    """Retorna o número de vezes que x aparece na lista L
    list, int ->int"""
    contador = 0
    for elemento in L:
        if elemento == x:
            contador+=1
    return contador

def remove_primeira_ocorrencia(L,x):
    """Remove a primeira ocorrencia de x na lista L
    list, int->list"""
    pos = 0 # posição da primeira ocorrencia
    while L[pos]!=x: # enquanto seja diferente percorre
        pos+=1

    del L[pos]  # remove a posição da primeira ocorrencia
    
def remove_condicional_V2(L,x):
    """Função que remove a primeira ocorrencia de x de uma lista
    quando aparace um número par de vezes
    list, int -> list
    """       
    ocorrencias = numero_ocorrencias(L,x) #quantaas vezes x está em L
    if ocorrencias % 2 == 0: #par
        remove_primeira_ocorrencia(L,x)

    return L
