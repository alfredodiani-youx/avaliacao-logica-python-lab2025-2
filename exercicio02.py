numeros=[] #váriavel que cria lista vazia
soma=0     #váriavel de soma que começa com valor 0
maior=0    #váriavel que armazena o maior número, começa com valor 0
menor=9999 #váriavel que armazena o menor número, começa com valor 9999
for c in range (0, 5): #laço for que roda sua estrutura 4 vezes
    numero=int(input('Digite um número')) #variável que recebe um número inteiro
    numeros.append(numero) #método que adiciona o valor da variável número na lista numeros
    if maior<numero:       #estrutura condicional que verifica se o número é maior ou não que o valor atribuido ao maior, caso seja, o valor maior será atualizado
        maior=numero
    if menor>numero: #estrutura condicional que verifica se o número é menor ou não que o valor atribuido ao menor, caso seja, o valor menor será atualizado
        menor=numero
    soma=soma+numero #cálculo que soma o valor armazenado na soma com o novo número inserido e armazena este novo valor em soma
media=soma/5 #variável que pega o valor final de todos os loops armazenado na soma e divide o por 5, tendo como resultado a média
print(f'LISTA FEITA! o maior número inserido foi {maior} o menor foi {menor} e a media dos números foi {media}') #print que mostra o maior numero inserido, o menor e a media dos numeros inseridos
print(f'Lista em ordem crescente {sorted(numeros)}') #print que retorna a lista em ordem crescente
print(f'Lista em ordem decrescente {sorted(numeros, reverse=True)}') #print que retorna a lista em ordem decrescente
verificacao= int(input('Insira um valor para verificarmos usa existencia na lista e sua posição')) #váriavel que pergunta ao usuário qual valor ele quer verificar a existência e a posição na lista
if verificacao in numeros: #estrutura condicional que impõe a condição de que se o valor selecionado na verificação estiver na lista números, o processo de verificação será ativado, caso o valor não esteja na lista será retornada uma mensagem informando que o vlaor não está na lista
    for i, valor in enumerate(numeros): #laço de repetição for que cria um contador de índice que atualiza a cada valor verificado na lista números
        if valor == verificacao: #estrutura condicional que impõe a condição de que quando o valor verificado no laço de repetição for igual ao valor selecionado pelo usuário para verificação o for se acaba e retorna uma mensagem mostrando o indice e a existencia do valor na lista
            print(f'O número {verificacao} está na posição {i}')
else:
    print(f'O número não esta na lista')