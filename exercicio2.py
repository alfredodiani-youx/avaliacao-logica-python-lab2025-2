
numeros = []


for i in range(5):
    valores = int(input(f"Digite valores: "))
    numeros.append(valores)


print(f"Lista digitada: {numeros}")

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)


print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")  # mostra média, menor e maior
print(f"Média dos valores: {media}")


print(f"Ordem crescente: {sorted(numeros)}")
print(f"Ordem decrescente: {sorted(numeros, reverse=True)}")    # mostra em ordem crescente e decrescente


busca = int(input("Digite um número para buscar na lista: "))

if busca in numeros:

    posicao = numeros.index(busca)
    print(f"O número {busca} está na lista, na posição {posicao}.")     # lê a lista e ve se o numero esta la ou não
else:
    print(f"O número {busca} não está na lista.")