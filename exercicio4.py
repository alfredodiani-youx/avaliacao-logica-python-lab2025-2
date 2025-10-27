'''
def analisarAluno(nome, notas):
    #função com o objetivo de ler as notas de um aluno, suas médias e definir uma situação
    #declarando o dicionário e seus elemntos + a lista das notas
    aluno = {}
    notas = []
    #adicionando as funcionalidades por meio de variáveis
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    media = (nota1 + nota2)/2
    #adicionando as notas na lista
    notas.append([nota1, nota2])
    #relacionando os valores da variáveis com os valores dentro do dicionário
    aluno['nome'] = nome
    aluno['media'] = media
    #validando os dados por meio de estrutura if e else. SE a média for menor que sete, o aluno está reprovado, se não, aprovado
    if aluno['media'] >= 7:
        aluno['situacao'] = 'APROVADO'
    else:
        aluno['situacao'] = 'REPROVADO'
    print(aluno)
analisarAluno('', '')
analisarAluno('',  '')
analisarAluno('', '')
'''
#alternativa que não precisa de um input. Transformo o parâmetro notas em uma lista, assim, consegue adiministrar mais de um valor
def analisarALuno(nome, *notas):
    #criando um dicionário e também seus elementos
    aluno = {}
    aluno['nome'] = nome
    media = sum(notas)/len(notas)
    aluno['media'] = media
    #fazendo a validação dos dados e definindo a situação do aluno
    if aluno['media'] >= 7:
        aluno['situacao'] = 'APROVADO'
    else:
        aluno['situacao'] = 'REPROVADO'
    #chamando os dados
    print(aluno)
#chamando a função
analisarALuno('Lucas', 8, 8)
analisarALuno('Coisa', 9, 9)
analisarALuno('Deivs', 5, 5)