numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\n--- Análise ---")
print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Média:", sum(numeros) / len(numeros))

print("\nOrdem Crescente:", sorted(numeros))
print("Ordem Decrescente:", sorted(numeros, reverse=True))

num_busca = int(input("\nDigite um número para buscar na lista: "))
if num_busca in numeros:
    print(f"O número {num_busca} está na lista na posição {numeros.index(num_busca)}.")
else:
    print("Número não encontrado na lista.")