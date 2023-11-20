
x = [[0,0],[0,0]]
y = [[0,0],[0,0]]
# crie uma matriz
# em python uma matriz são listas dentros de listas

x[0][0], y[0][0], x[0][1], y[0][1] = input().split(" ", 3)
x[1][0], y[1][0], x[1][1], y[1][1] = input().split(" ", 3)
# usei o split() para poder a cada espaço ele atribuir o numero a
# uma variavel diferente(no caso um espaço diferente da matriz)
# o numero dentro do split é para indicar quantas vezes ele vai separar
# usei 3 pois ele conta o 0, então 0,1,2,3 são 4 numeros
#
# obs: eu poderia fazer de uma forma diferente, mas no ex
# dizem que os numeros podem variar de 0 a 1 milhão

for i in range(0, 2):
	for j in range(0, 2):
		x[i][j] = int(x[i][j])

for i in range(0, 2):
	for j in range(0, 2):
		y[i][j] = int(y[i][j])

# Acima eu estou convertendo os numeros(que por enquanto são str)
# para int(inteiro), para poder abaixo fazer a comparação(que é numerica)
# preciso converter porque o input le qualquer entrada como string

if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1] > x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
	print(0)
else:
	print(1)

# agora acontece a comparação para saber o resultado