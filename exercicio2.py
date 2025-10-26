listaNumero = []

for l in range(5):
    
    numero = int(input(f'Digite o {l+1} numeros inteiros: '))
    listaNumero.append(numero)

media = sum(listaNumero) / 5
num_cresente = sorted(listaNumero)
num_decrescente = sorted(listaNumero, reverse=True)

print(f'Maior numero: {max(listaNumero)}')
print(f'Menor numero: {min(listaNumero)}')
print(f'Media dos numeros: {media}')

print(f'Lista em ordem cresente: {num_cresente}')
print(f'Lista em ordem decrescente {num_decrescente}')

while True:

    numero_lista = int(input('Digite um numero para verificar se esta na lista: '))

    if numero_lista in listaNumero:

        posicoes = listaNumero.index(numero_lista)
        print(f'o numero {numero_lista} esta na lista.')

    else:

        print(f'o numero {numero_lista} nao esta na lista.')