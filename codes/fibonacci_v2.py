# Esse código calcula a sequência de Fibonacci
anterior=1
atual=1
total=0

N=int(input('Digite N: '))

while (total<N):
	proximo = anterior + atual
	anterior = atual
	atual = proximo
	 
	print(anterior, atual, proximo)
	total=total+1