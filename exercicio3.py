boletim = list()

while True:
    nome = str(input('Digite o seu nome: '))
    nota1 = int(input('Digite a sua 1° nota: '))
    nota2 = int(input('Digite a sua 2° nota: '))
    media = (nota1+nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    print('-' * 30)

    if continuar in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":<16}')

for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<12}{a[2]:<16.1f}')
while True:
    numeroAluno = int(input('Mostrar notas de quais alunos? (111 interrompa)'))
    if numeroAluno == 111:
        print('Fim')
        break
    if numeroAluno <=len (boletim) -1:
        print(f'Notas de {boletim[numeroAluno][1]}')
print('Volte sempre!')