inteiros = list()
contador = 0
while contador < 5:
    numeros = int(input('Digite um número inteiro: '))
    contador += 1
    inteiros.append(numeros)

maior = max(inteiros)
menor = min(inteiros)
media = sum(inteiros) / len(inteiros)
crescente = sorted(inteiros)
decrescente = sorted(inteiros, reverse=True)

print(f'O maior número entre os digitados é {maior}')
print(f'O menor número entre os digitados é {menor}')
print(f'A média entre os números digitados é {media:.2f}')
print(f'Eles em ordem crescente são {crescente}')
print(f'E eles em ordem decrescente são {decrescente}')

escolha = int(input('Agora me diga algúm número: '))
print(escolha)
if escolha in inteiros:
    posicaoEscolhida = inteiros.index(escolha)
    print(f'O número {escolha} está presente na lista e está na posição {posicaoEscolhida}!')
else:
    print(f'O número {escolha} não está presente na lista!')