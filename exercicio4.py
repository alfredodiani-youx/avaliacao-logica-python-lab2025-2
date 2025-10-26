def analisarAluno(nome, notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    return {"nome": nome, "media": media, "situacao": situacao}

alunos = []

for c in range(1, 4):
    print('-' * 30)
    nome = str(input(f'Digite o nome do {c}º aluno: '))

    notasAluno = []
    for n in range(1, 3):
        notas = float(input(f'Digite sua {n}ª nota: '))
        notasAluno.append(notas)

    informacoesAluno = analisarAluno(nome, notasAluno)
    alunos.append(informacoesAluno)

print('-' * 30)
for aluno in alunos:
    print(f"Nome: {aluno['nome']} - Média: {aluno['media']:.1f} - Situação: {aluno['situacao']}")