boletim = list()

while True:
    nome = str(input('Digite o seu nome: ')).capitalize()
    nota1 = int(input('Digite a sua 1° nota: '))
    nota2 = int(input('Digite a sua 2° nota: '))

    media = (nota1+nota2) / 2

    boletim.append([nome, [nota1, nota2], media])

    continuar = str(input('\033[34mDeseja continuar? [S/N] \033[m')).lower().strip()[0] # retira os espaços
    print('-' * 30)

    if continuar in 'Nn':
        break
print(f'\033[35m{"Nº.":<6}{"NOME":<12}{"MÉDIA":<16}\033[m')

for indice, aluno in enumerate(boletim):
    print(f'{indice:<6}{aluno[0]:<12}{aluno[2]:<16.1f}')

while True:
    numeroAluno = int(input('\033[33mMostrar notas de quais alunos? (111 interrompa)\033[m'))

    if numeroAluno == 111:
        print('Fim')
        break

    if numeroAluno <=len (boletim) -1:
        print(f'Notas {boletim[numeroAluno][0]}: {boletim[numeroAluno][1]}')
print('Volte sempre!')