continuacao= 'S'
boletim= []
while continuacao == 'S':
    nome=(str(input(f'Digite o nome do aluno: ')).upper())
    nota1=(float(input(f'Digite a primeira nota do aluno: ')))
    nota2=(float(input('Digite a segunda nota do aluno: ')))
    aluno=[nome, [nota1, nota2]]
    boletim.append(aluno)
    continuacao=str(input('Você deseja continuar inserindo novos alunos? [S/N] ').upper())

verificacao= str(input('Digite o nome do aluno que você quer olhar').upper())
for aluno in boletim:
    if aluno[0].upper() == verificacao:
        media= (aluno[1][0]+ aluno[1][1])/2
        print(f'As notas do aluno {verificacao} são {aluno[1][0]} e {aluno[1][1]} e sua média é {media}')