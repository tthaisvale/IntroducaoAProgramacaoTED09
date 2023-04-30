numeros = []

for i in range (20):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

    numeros_invertidos = numeros[::-1]

    print('Números lidos na ordem inversa: ')
    for numero in numeros_invertidos:
        print(numero)
