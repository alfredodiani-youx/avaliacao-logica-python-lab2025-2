def analisar_aluno(nome, notas):
    media = (notas[0] + notas[1]) / 2
    return {"nome": nome, "media": media}

alunos = []

for i in range(3):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    aluno = analisar_aluno(nome, [nota1, nota2])
    alunos.append(aluno)

print('---Boletim da turma:---')
for aluno in alunos:
    print("Nome:", aluno["nome"], "/ Média:", aluno["media"])