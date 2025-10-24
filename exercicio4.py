def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    return {'nome': nome, 'media': media, 'situacao': situacao}


alunos = []

print("=== Cadastro de Alunos ===")
for i in range(3):
    print(f'\nAluno {i+1}')
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno = analisar_aluno(nome, [n1, n2])
    alunos.append(aluno)

print("\n=== RELATÓRIO FINAL ===")
print('Nome\t\tMédia\tSituação')
for a in alunos:
    print(f'{a["nome"]:<15}{a["media"]:<6.1f}{a["situacao"]}')


