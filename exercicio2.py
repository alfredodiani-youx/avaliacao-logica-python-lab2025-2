numeros = []

for i in range(5):
    valor = int(input('Digite um número: '))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / 5

print(f'Maior número: {maior}')
print(f'Mnor número: {menor}')
print(f'Média: {media} ')

print(f'Ordem crescente: {sorted(numeros)}')
print(f'Ordem decrescente: {sorted(numeros, reverse=True)}')
procurar_numeros= int(input("Digite um número para procurar: "))

if procurar_numeros in numeros:
    posicao = numeros.index(procurar_numeros)
    print(f'O número está na lista e está na posição: {posicao}')
else:
    print('Esse número não está na lista.')