def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    return{"nome": nome, "media": media, "situacao": situacao}

#Programa Principal

alunos = [] #guardar os dados do dicionário
for i in range(0, 3):
    nome = str(input('>> Nome do aluno: '))
    print('-'*40)

    notas = []
    continuarNotas = 'S'
    while continuarNotas == 'S':
        nota = float(input(f'Nota do aluno {nome}: '))
        print('-'*40)
        notas.append(nota)
        continuarNotas = str(input('Deseja adicionar outra nota? [S/N]: ')).upper().strip()
        print('-'*40)
    alunos.append(analisar_aluno(nome, notas))



print()
print(' ALUNOS')
print('-'*40)
for estudante in alunos:
    print(f' Nome: {estudante["nome"]}')
    print(f' Média: {estudante["media"]:.1f}')
    print(f' Situação: {estudante["situacao"]}')
    print('-'*40)




