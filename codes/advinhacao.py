import random
def jogo_adivinhacao(max_tentativas = 5, limite = 100):
    numero_secreto = random.randint(1, limite) # Gera um número aleatório
    tentativas = 0
    print(f"Tente adivinhar o número entre 1 e {limite}.")
    while tentativas < max_tentativas:
        chute = int(input("Digite um número: "))
        if chute == numero_secreto:
            print("Parabéns! Você acertou!")
            break #sai do while
        elif chute < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
            tentativas += 1
        if tentativas == max_tentativas:
            print("Suas tentativas acabaram. O número secreto era:", numero_secreto)
            print("O jogo acabou")
        
#Função main
def main():
    # entrada de dados    
   # numero = int(input('digite o número para a função fibonacci: '))
          
    # processamento
    jogo_adivinhacao()
               
    # saida

#Testando a função
main()