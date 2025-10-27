numeros = []
for n in range(0, 5):
    n = int(input('Digite um numero: '))
    numeros.append(n)
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)
print(f"Números digitados: {numeros}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")
print(f"A ordem crescente é: {sorted(numeros)}")
print(f"A ordem decrescente é: {sorted(numeros, reverse=True)}")
num_busca = int(input("Digite um numero para verificar se está na lista: "))

if num_busca in numeros:
    posicoes = [i for i, v in enumerate(numeros) if v == num_busca]#enumerate: adicionei um contador a um iterável
    print(f"O número {num_busca} está na lista nas posições: {posicoes}")
else:
    print(f"O número {num_busca} não está na lista.")