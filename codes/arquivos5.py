# Abre o arquivo de entrada
with open("funcionarios.txt", "r") as arquivo_entrada:
        
    # Lê todas as linhas do arquivo
    linhas = arquivo_entrada.readlines()
    # Itera sobre as linhas
    for linha in linhas:
        # Separa as informações de cada funcionário
        funcionario = linha.strip().split(",")
        
        # Imprime as informações na tela
        print(f"Nome: {funcionario[0]}")
        print(f"Idade: {funcionario[1]}")
        print(f"Gênero: {funcionario[2]}\n")
        #print()
        
# Cria um novo arquivo de saída
with open("funcionarios_com_salario.txt", "w") as arquivo_saida:
    # Itera sobre as linhas do arquivo de entrada novamente
    for linha in linhas:
        # Separa as informações de cada funcionário
        funcionario = linha.strip().split(",")
        
        # Calcula um salário fictício para o funcionário
        salario = int(funcionario[1]) * 1000
        
        # Escreve as informações do funcionário e o salário no novo arquivo
        arquivo_saida.write(f"{funcionario[0]}, {funcionario[1]}, {funcionario[2]}, {salario}\n")