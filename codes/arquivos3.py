multiplos4 = open('multiplos4.txt','w')
pares = open('pares.txt')

for linha in pares.readlines():
    if int(linha) % 4 == 0:
        multiplos4.write(linha)
        #print(linha)

pares.close()
multiplos4.close()