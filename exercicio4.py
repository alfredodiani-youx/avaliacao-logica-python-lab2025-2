def analisar_aluno(nome, notas):

    media = sum(notas) / len(notas)
    if media >= 7:
        condicao = "\033[32mAPROVADO\033[m"

    elif media >= 5:
        condicao = "\033[31mREPROVADO\033[m"
    else:
        condicao = "Reprovado"
    return {"nome": nome, "media": media, "condicao": condicao}

alunos = []

for nomeAluno in range(3):
    nome = str(input("Qual o nome do aluno: "))
    
    notas = []
    for notasAluno in range(3):

        nota = float(input(f'Qual a {notasAluno+1}° nota do {nome}: '))
        notas.append(nota)
        
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)