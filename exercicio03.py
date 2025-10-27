continuacao= 'S' #variavel de continuação que tem como valor a string 'S'
boletim= [] #variável que cria uma lista vazia
while continuacao == 'S': #estrutura de repetição que cria um loop enquanto continuação for 'S'
    nome=(str(input(f'Digite o nome do aluno: ')).upper()) #variável que recebe o nome do aluno
    nota1=(float(input(f'Digite a primeira nota do aluno: '))) #variável que recebe a nota 1 do aluno
    nota2=(float(input('Digite a segunda nota do aluno: '))) #variável que recebe a nota 2 do aluno
    aluno=[nome, [nota1, nota2]] #variável que cria uma lista com todos os dados do aluno
    boletim.append(aluno) #método que adiciona a lista aluno na lista boletim, formando listas compostas
    continuacao=str(input('Você deseja continuar inserindo novos alunos? [S/N] ').upper())

verificacao= str(input('Digite o nome do aluno que você quer olhar').upper()) #variável que recebe o nome do aluno que o usuário quer verificar
for aluno in boletim: #laço de repetição que verifica cada lista na lista boletim
    if aluno[0].upper() == verificacao: #estrutura condicional que impõe a condição de que se o nome do aluno for igual ao nome do aluno selecionado pelo usuário para verificação
        media= (aluno[1][0]+ aluno[1][1])/2 #é calculado atráves da variável media sua media, somando a nota 1 e 2 do aluno e dividindo as por 2
        print(f'As notas do aluno {verificacao} são {aluno[1][0]} e {aluno[1][1]} e sua média é {media}')#print formatado que retorna o nome do aluno, suas notas e sua média