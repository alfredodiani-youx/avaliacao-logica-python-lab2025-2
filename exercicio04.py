def analisarAluno(n, d, e):
    aluno={}
    media= (d+e)/2
    if media >= 5.0:
        situacao= 'Aprovado'
    else:
        situacao='Reprovado'
    aluno['NOME']= n
    aluno['MEDIA']= media
    aluno['SITUAÇÃO']= situacao
    return aluno


for c in range (1, 4):
    nome=str(input('Digite o nome do aluno: '))
    nota1= float(input('Digite a nota 1 do aluno: '))
    nota2= float(input('Digite a nota do 2 aluno: '))
    print(f'A análise do aluno é: {analisarAluno(nome, nota1, nota2)} ')