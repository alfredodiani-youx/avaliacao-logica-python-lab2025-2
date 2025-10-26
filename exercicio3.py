alunos = []

while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    if input("Quer continuar? [S/N] ").upper() == "N":
        break

print('Boletim da turma:')
print('Posição  Nome           Média')
print('-' * 30)
for posicao, aluno in enumerate(alunos):
    print(f'{posicao:<8}{aluno[0]:<15}{aluno[2]:>7.1f}')

while True:
    opcao = int(input('Digite o número da posição do aluno (999 para sair): '))
    if opcao == 999:
        break
    if 0 <= opcao < len(alunos):
        print(f'Notas de {alunos[opcao][0]}: {alunos[opcao][1]}')