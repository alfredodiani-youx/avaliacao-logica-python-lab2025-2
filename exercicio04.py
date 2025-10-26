def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "nome": nome,
        "media": round(media, 1),
        "situacao": situacao
    }

# Programa principal
alunos = []

print("--- Cadastro de Alunos ---")
for i in range(3):
    print(f"\nAluno {i + 1}:")
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    
    alunos.append(analisar_aluno(nome, [nota1, nota2]))

print("\n--- RELATÓRIO FINAL ---")
for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Média: {aluno['media']} | Situação: {aluno['situacao']}")