numeros = []
for i in range(5):
    while True:
        try:
            inteiros = int(input(f'Digite o {i+1}º número inteiro: '))
            break
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
    numeros.append(inteiros)

print(numeros)
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média: {media:.2f}')

crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)
print(f'Lista em ordem crescente: {crescente}')
print(f'Lista em ordem decrescente: {decrescente}')

while True:
    try:
        busca = int(input('Digite um número para verificar se ele está na lista: '))
        break
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

posicoes = [i + 1 for i, v in enumerate(numeros) if v == busca]
if posicoes:
    pos_str = ', '.join(str(p) for p in posicoes)
    print(f'O número {busca} está na lista nas posição(ões): {pos_str}.')
else:
    print(f'O número {busca} não está na lista.')