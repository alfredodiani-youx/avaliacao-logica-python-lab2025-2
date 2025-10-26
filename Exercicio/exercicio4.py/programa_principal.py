import analisar_alun
alunos = []

print("=== Cadastro de 3 alunos ===")
for i in range(3):
    nome = input(f"\nNome do {i+1}º aluno: ")
    notas = []
    for j in range(2):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    aluno = analisar_alun.analisar_aluno(nome, notas)
    alunos.append(aluno)
print("\n=== RELATÓRIO FINAL ===")
print(f"{'Nome':<15}{'Média':>8}{'Situação':>15}")
print("-" * 40)
for a in alunos:
    print(f"{a['nome']:<15}{a['media']:>8.2f}{a['situacao']:>15}")