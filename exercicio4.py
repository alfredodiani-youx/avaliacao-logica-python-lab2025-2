def analisar_aluno(nome, notas):
    """
    Recebe o nome e uma lista de notas,
    calcula a média e retorna um dicionário com nome, média e situação.
    """
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return {"nome": nome, "media": media, "situacao": situacao}
alunos = []
for i in range(3):
    print(f"\nAluno {i + 1}:")
    nome = input("Nome: ")
    notas = []
    for j in range(2):
        nota = float(input(f"Nota {j + 1}: "))
        notas.append(nota)
    alunos.append(analisar_aluno(nome, notas))
print("\n=== RELATÓRIO DE ALUNOS ===")
for a in alunos:
    print(f"Nome: {a['nome']:<10} | Média: {a['media']:.1f} | Situação: {a['situacao']}")
