alunos = []  # Lista principal

while True:
    nome = str(input("Nome do aluno: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, [nota1, nota2]]) 

    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == 'N':
        break

print("-=" * 30)
print(f'{"Nº":<4}{"NOME":<20}{"MÉDIA":>8}')
print("-" * 34)

for i, aluno in enumerate(alunos):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{i:<4}{aluno[0]:<20}{media:>8.1f}')

print("-" * 34)


while True:
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        break
    if opc >= len(alunos) or opc < 0:
        print("Número inválido. Tente novamente.")
    else:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
        print("-" * 34)

print("<<< ACABOU >>>")