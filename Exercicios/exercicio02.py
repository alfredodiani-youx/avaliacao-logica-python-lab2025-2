listadenumeros = []
for c in range(5):
    numero = int(input(f"Digite o {c+1}º número: "))
    listadenumeros.append(numero)

media = sum(listadenumeros) / len(listadenumeros)
print(f"Lista original: {listadenumeros}")
print(f'O maior valor encontrado na lista é :{max(listadenumeros)}\nÉ o menor valor encontrado é {min(listadenumeros)}')
print(f"A média dos valores é: {media:.2f}")

crescente = sorted(listadenumeros)
decrescente = sorted(listadenumeros, reverse=True)
print(f"Lista em ordem crescente: {crescente}\nLista em ordem decrescente: {decrescente}")

numero_busca = int(input("Digite um número para verificar se ele está na lista: "))

if numero_busca in listadenumeros:
    posicao = listadenumeros.index(numero_busca)
    print(f"O número {numero_busca} está na lista na posição {posicao}.")
else:
    print(f"O número {numero_busca} NÃO está presente na lista.")
