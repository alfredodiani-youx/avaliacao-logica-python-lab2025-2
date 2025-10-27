def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    return {"nome": nome, "media": media, "situacao": situacao}


relatorio = []

for i in range(3):
    print(f"Aluno {i+1}:")
    nome = input("Nome: ")
    notas = []
    for n in range(3):
        nota = float(input(f"Nota {n+1}: "))
        notas.append(nota)
    
    aluno = analisar_aluno(nome, notas)
    relatorio.append(aluno)

print("--- RELATÓRIO FINAL ---")
for aluno in relatorio:
    print(f"Nome: {aluno['nome']} -|- Média: {aluno['media']:.1f} -|- Situação: {aluno['situacao']}")