continuar = 'S'
alunos = []
listaNotas = []
listaNomes = []
while continuar == 'S':
    estudante = str(input('>> Digite o nome do aluno: '))
    alunos.append(estudante)
    listaNotas = []
    continuarNotas = 'S'
    while continuarNotas == 'S':
        print('-'*35)
        nota = float(input(f'>> Digite a nota do aluno {estudante}: '))
        listaNotas.append(nota)
        print('-'*35)
        continuarNotas = input('Deseja adicionar outra nota? [S/N]: ').upper().strip()

    alunos.append(listaNotas)
    listaNomes.append([estudante, listaNotas.copy()])
    print('-'*35)
    continuar = input('Deseja adicionar outro aluno? [S/N]: ').upper().strip()

print('-'*35)
print(' BOLETIM')
print(f"{'Nº':<3}{'ALUNO':>10}{'MÉDIA':>6}")

indice = 0
for indice, aluno in enumerate(listaNomes):
    nome = aluno[0]
    notas = alunos[1]
    media = sum(listaNotas) / len(listaNotas)
    print(f'{indice:<3}{nome:>10}{media:>6.1f}')

print('-'*35)
consultarNotas = 'S'
while consultarNotas != 'N':
        consulta = input('Digite o Nº do índice para obter as notas do aluno: ')
        indice = int(consulta)

        if 0 <= indice < len(listaNomes):
            alunodados = listaNomes[indice]
            estudante = alunodados[0]
            notas = alunodados[1]

            print('-'*35)
            print(f'Estudante: {nome}.\nNotas: {notas}.\nMédia: {media}.')
            print('-'*35)
            
        else: 
            print('-'*35)
            print('Índice inválido.')
            print('Digite um Nº de índice válido para obter as notas do aluno!')

            
            print("-" * 35)
        consultarNotas = input('Deseja consultar outro aluno? [S/N]: ').upper().strip()
        print("-" * 35)      
        if consultarNotas == 'N':
            print('Finalizando...')
            break

