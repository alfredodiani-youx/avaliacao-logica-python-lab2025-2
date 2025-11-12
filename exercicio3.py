alunos = []
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2]])
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    media = sum(a[1]) / 2
    print(f'{i:<4}{a[0]:<15}{media:>8.1f}')
print('-' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc >= 0 and opc < len(alunos):
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
    else:
        print('Índice inválido. Tente novamente.')
print('<<< PROGRAMA ENCERRADO >>>')
