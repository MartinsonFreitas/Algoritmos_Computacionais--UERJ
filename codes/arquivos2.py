impares = open('impares.txt','w')
pares = open('pares.txt','w')

for n in range(0,200):
    if n % 2 == 0:
        pares.write('%d\n' % n)
    else:
        impares.write('%d\n' % n)

impares.close()
pares.close()