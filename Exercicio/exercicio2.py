numeros = []

for i in range (0, 5):
    numeros_digitados = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numeros_digitados)
maior = max(numeros)
menor = min(numeros)
medio = sum(numeros) / len(numeros)


print ()
print (f'=-' * 40)
print (f'Os números são {numeros}, o  maior valor é {maior},o menor valor é {menor}, A media dos valores é {medio}')
print ()
print (f'Ordem crescente: {sorted(numeros)}')
print (f'Ordem decrescente: {sorted(numeros, reverse=True)}')

busca = int(input('Digite um número para procurar na busca: '))

if busca in numeros:
    numero_buscado = numeros.index(busca)
    print (f'O número esta na posição {numero_buscado + 1}')
else:
    print (f'Este número não foi adicionado na lista')