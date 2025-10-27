listaNumero = []

for c in range (0,5):
    listaNumero.append(int(input('Escolha um número:\n->')))

print(f'O maior número foi: {max(listaNumero)}')
print(f'O menor número foi: {min(listaNumero)}')
print(f'A média foi {sum(listaNumero)/5}')

print('Os números selecionados organizados em ordem crescente')
listaNumero.sort()
print(listaNumero)

print('Os números selecionados organizados em ordem decrescente')
listaNumero.sort(reverse=True)
print(listaNumero)

numeroEscolhido = int(input('Escolha um número e diremos se ele esta na lista:\n->'))
if numeroEscolhido in listaNumero:
    print(f'{numeroEscolhido} está na lista e na posição {listaNumero.index(numeroEscolhido)}!')
else:
    print(f'{numeroEscolhido} não está na lista!')

#Utilizei o for c in range para repetir 5 vezes a ação de adicionar número
#Logo em seguida utilizei as funções:
# min (para selecionar o menor número),
# max (para selecionar o maior número),
# sum (para somar todos os números da lista)
# .sort (para organizar a lista tanto de forma normal, quanto ao contrário reverse=True) e
# .index (para mostrar a posição do número escolhido na lista
#Fiz um sistema para se houver o número escolhido na lista ele da uma resposta informando que há e sua posição e se não outra resposta indicando que não está na lista