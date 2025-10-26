alunos = []

while True:
    nome = str(input('Digite o nome aluno: '))
    notaUm = float(input('Digite a primeira nota: '))
    notaDois = float(input('Digite a segunda nota: '))
    media = (notaUm + notaDois) / 2

    alunos.append([nome, [notaUm, notaDois], [media]]) 

    print('-' * 30)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

    if continuar not in 'Ss':
        break
    print('-' * 30)

print('-' * 30)
print(f'Pos {"NOME":^10} {"MÉDIA":^20}')
print('-' * 30)

for indice, aluno in enumerate(alunos):
    print(f'{indice} {str(alunos[indice][0]):^12} {str(alunos[indice][2]):^20}')

print('-' * 30)

while True:
    notaIndividual = int(input(f'Qual aluno deseja ver as notas indivíduais? (Digite -1 para interromper) '))

    if notaIndividual == -1:
        print('-' * 30)
        print('Programa Finalizado.')
        print('-' * 30)
        break

    elif 0 <= notaIndividual < len(alunos):
        print('-' * 30)
        print(f'Notas de {alunos[notaIndividual][0]}')
        print(f'{alunos[notaIndividual][1]}')
        print('-' * 30)

    elif notaIndividual not in alunos:
        print('Não há nenhum aluno neste indíce.')
        print('-' * 30)