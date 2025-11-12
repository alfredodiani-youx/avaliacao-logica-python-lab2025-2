numeros = []
for i in range(5):
    while True:
        try:
            n = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(n)
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)
print("\n--- Resultados ---")
print(f"Números digitados: {numeros}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")
print(f"Ordem crescente: {sorted(numeros)}")
print(f"Ordem decrescente: {sorted(numeros, reverse=True)}")
try:
    busca = int(input("\nDigite um número para procurar na lista: "))
    if busca in numeros:
        posicao = numeros.index(busca)
        print(f"O número {busca} está na lista, na posição {posicao}.")
    else:
        print(f"O número {busca} não foi encontrado na lista.")
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")