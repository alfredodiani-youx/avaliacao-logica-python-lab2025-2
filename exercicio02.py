numeros=[]
soma=0
maior=0
menor=9999
for c in range (0, 5):
    numero=int(input('Digite um número'))
    numeros.append(numero)
    if maior<numero:
        maior=numero
    if menor>numero:
        menor=numero
    soma=soma+numero
media=soma/5
print(f'LISTA FEITA! o maior número inserido foi {maior} o menor foi {menor} e a media dos números foi {media}')
print(f'Lista em ordem crescente {sorted(numeros)}')
print(f'Lista em ordem decrescente {sorted(numeros, reverse=True)}')
verificacao= int(input('Insira um valor para verificarmos usa existencia na lista e sua posição'))
if verificacao in numeros:
    for i, valor in enumerate(numeros):
        if valor == verificacao:
            print(f'O número {verificacao} está na posição {i}')
else:
    print(f'O número não esta na lista')