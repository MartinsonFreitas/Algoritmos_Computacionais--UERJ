"""arquivo = open('numeros.txt','a')

for linha in range(1,10):
    arquivo.write('%d\n' % linha)
    
arquivo.close()"""

"""
Tratamento de ERROS!

Try:
    {SEU CODIGO AQUI --> TEnta fazer algo}
Except:
    {Seu código aqui --> Em caso de erro fazer algo aqui}
Finally:
    {Executa algo aqui --> Fecha algo...}
"""
    
# Abre um arquivo no modo 'w' para escrever nele
# Abre um arquivo no modo "r" para ler seu conteúdo
arquivo = open('numeros.txt','r')
soma = 0

for linha in arquivo.readlines():
    #print(linha)
    conteudo = linha.replace('\n', '')
    soma += float(linha)
    arquivo.close()
    
print('Total:',soma)
    
#teste
