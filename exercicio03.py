alunos = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, [nota1, nota2]])
    
    op = input("Deseja continuar? [S/N]: ").upper()
    if op == 'N':
        break

print("\n--- Boletim Geral ---")
print("Nº  Nome      Média")
print("-" * 20)
for i, a in enumerate(alunos):
    media = sum(a[1]) / 2
    print(f"{i}  {a[0]:<10} {media:.1f}")

while True:
    indice = int(input("\nMostrar notas de qual aluno? (999 interrompe): "))
    if indice == 999:
        break
    if indice < len(alunos):
        print(f"Notas de {alunos[indice][0]}: {alunos[indice][1]}")
    else:
        print("Índice inválido!")