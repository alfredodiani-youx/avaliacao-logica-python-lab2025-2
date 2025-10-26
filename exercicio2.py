#criando lista
lista = []
#começando um laço de repetição, while perpétuo com condição True
while True:
    print('='*30)
    #outro laço de repetição, dessa vez um for, feito para adicionar os números na lista
    for contador in range(1, 6):
        numero = int(input(f'Digite o valor desejado na posição {contador}: '))
        lista.append(numero)
    print('='*30)
    #variável para calcular a média dos números da lista
    media = sum(lista)/len(lista) 
    #laço de repetição criado para o processo de busca de um número dentro da lista
    while True:
        #variável criada para procurar o número dentro da lista
        ver = int(input('Digite o número que você procura: '))
        #validação dos dados por meio de if e else
        if ver not in lista:
            print(f'O valor {ver} não está presente. ')
        else:
            #se o dado estiver na lista, ele será encontrado e sua posição será indicada na variável pos
            #usamos o comando index(x) para facilitar o processo
            pos = lista.index(ver)
            #quebra do processo após encontrar o número
            break
    #após definir os 5 números da lista e encontrar o número desejado, é usado o break para quebrar o ciclo
    break
#organização das listas
listaOrdenada = sorted(lista)
listaReversa = sorted(lista, reverse=True)
#encontrando o maior e o menor número da lista
maior = max(lista)
menor = min(lista)
print('='*30)
#apresentação dos dados
print(f'''A lista é: {lista}
A lista em ordem crescente é {listaOrdenada}
Em ordem decrescente é {listaReversa}
O maior valor é {maior}
O menor valor é {menor}            
O valor {ver} está na posição {pos + 1}
''')