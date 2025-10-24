numeros = []
numeroMaior = 0
numeroMenor = 0

for n in range(5):
    numeros.append(int(input('Digite um número: ')))
    media = sum(numeros) / len(numeros)
    numeroMaior = max(numeros)
    numeroMenor = min(numeros)

print('*-'*20)
print(f' - Média dos números: {media}\n - Maior número: {numeroMaior}\n - Menor número: {numeroMenor}')
print('*-'*20)

ordemCrescente = sorted(numeros)
ordemDecrescente = sorted(numeros, reverse = True)
print(f' - Lista dos números em ordem crescente: {ordemCrescente}')
print(f' - Lista dos números em ordem decrescente: {ordemDecrescente}')
posicaoNumero = int(input('Fale um número que está na lista: '))

if posicaoNumero in numeros:
    posicao = numeros.index(posicaoNumero)
    print(f' - Esse número está na lista! E está posicionado na {posicao}ª posicao -')
else:
    print(' - Esse número não está na lista. - ')