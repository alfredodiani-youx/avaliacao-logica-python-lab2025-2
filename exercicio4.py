def analisar_aluno(nome, notas): # def definição de função

    media = sum(notas) / len(notas)
    if media >= 7:
        condicao = "Aprovado"

    elif media >= 5:
        condicao = "Recuperação"

    else:
        condicao = "Reprovado"
    return {"nome": nome, "media": media, "condicao": condicao}

alunos = []

for nomeAluno in range(3):
    nome = str(input("Qual o nome do aluno(a): "))
    
    notas = []
    for notasAluno in range(3): # for = para ou por

        nota = float(input(f'Qual a {notasAluno+1}° nota do(a) {nome}: '))
        notas.append(nota)
        
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)


print("\n\033[36mDICIONÁRIO DE ALUNOS\033[m")

for aluno in alunos:

    print(f"Nome:{aluno['nome']}")
    print('-' * 30)
    print(f"Média:{aluno['media']:.2f}")
    print('-' * 30)
    print(f"Condição:{aluno['condicao']}")
    print('-' * 30)