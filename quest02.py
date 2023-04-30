vet = []

for i in range (10):
    n = int(input('Digite um número: '))
    vet.append(n)

repetidos = []

for i in range(len(vet)):
    for j in range(i+1, len(vet)):
        if vet[i] == vet[j] and vet[i] not in repetidos:
            repetidos.append(vet[1])
            print('Número repetido: ', vet[i])
    for r in repetidos:
        posicoes = []
    for i in range (len(vet)):
        if vet[i] == r:
            posicoes.append(i)
            print('Posições do número' , r, 'no vetor: ', posições)


