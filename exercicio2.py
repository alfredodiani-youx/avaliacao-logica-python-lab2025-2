numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print("\nMaior:", maior)
print("Menor:", menor)
print("Média:", round(media, 2))

print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))

busca = int(input("\nDigite um número para verificar se está na lista: "))

if busca in numeros:
    print(f"O número {busca} está na posição {numeros.index(busca)}")
else:
    print("NÚMERO NÃO ENCONTRADO NA LISTA.!")
