numerosInteiros = []
maiorInteiro = 0
menorInteiro = 0
for numero in range(5):
    numerosInteiros.append(int(input('>> Digite um número inteiro: ')))
    mediaNumeros = sum(numerosInteiros) / len(numerosInteiros)
    menorInteiro = min(numerosInteiros)
    maiorInteiro = max(numerosInteiros)

print('-'*30)
print('         RESULTADO    ')
print('-'*30)
print(f'    Maior número: {maiorInteiro}.')
print(f'    Menor número: {menorInteiro}.')
print(f'    Média dos números: {mediaNumeros}.')
print(f'    Lista em ordem crescente: {sorted(numerosInteiros)}.')
numerosInteiros.sort(reverse=True)
print(f'    Lista em ordem decrescente: {numerosInteiros}.')
numeroposicao = int(input('>> Digite um número para buscar na lista: '))
if numeroposicao in numerosInteiros:
    posicao = numerosInteiros.index(numeroposicao)
    print(f'  O número digitado está na lista! E está na {posicao}ª posição.')
else:
    print(f' O número digitado não está na lista!')






