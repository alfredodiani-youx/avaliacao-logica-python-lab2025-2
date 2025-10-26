listaNumeros = []

for c in range(1, 6):
    numeros = int(input(f'Digite o {c}º número: '))
    listaNumeros.append(numeros)

media = sum(listaNumeros) / c
listaCrescente = sorted(listaNumeros)
listaDecrescente = sorted(listaNumeros, reverse=True)

print('-' * 25)
print(f'O maior número digitado foi {max(listaNumeros)}.')
print(f'O menor número digitado foi {min(listaNumeros)}.')
print(f'A media com todos os valores digitados é {media:.0f}.')

print(f'Os números digitados de forma crescente são: {listaCrescente}')
print(f'Os números digitados de forma decrescente são: {listaDecrescente}')

print('-' * 25)

while True:
    print('-' * 25)
    pedirNumero = int(input('Qual o número que você deseja ver da Lista? (Digite -1 para encerrar) '))

    if pedirNumero == -1:
        print('Programa Encerrado.')
        break

    if pedirNumero in listaNumeros:
        print(f'O número {pedirNumero} está na lista, e está na posição ', end='')
        for indice, valor in enumerate(listaNumeros):
            if valor == pedirNumero:
                print(indice + 1, end=' ')  
        print()

    if pedirNumero not in listaNumeros:
        print(f'O número {pedirNumero} não está na lista.')