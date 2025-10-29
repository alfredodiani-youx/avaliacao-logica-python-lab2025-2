numeros = []

for c in range(0, 5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    maiorNumero = max(numeros)
    menorNumero = min(numeros)
    media = sum(numeros) / len(numeros)

print('-' * 55)
print(f'Lista de números: {numeros}')
print('-' * 55)
print(f'A média é {media}')
print('-' * 55)
print(f'O maior número é {maiorNumero}')
print('-' * 55)
print(f'O menor número é {menorNumero}')
print('-' * 55)

numeros.sort()
print(numeros)
print('-' * 55)

numeros.sort(reverse = True)
print(f'\033[34m{numeros}\033[m')
print('-' * 55)
