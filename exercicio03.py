alunos = []
continuar = 'S'

while continuar == 'S':
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    alunos.append([nome, [nota1,nota2]])
    continuar = input('Quer cadastrar outro aluno? [Ss/Nn]').upper()

print(' ----- B o l e t i m -----')
print('Nº      N O M E      M É D I A')
print('-----------------------------')

for n in range(len(alunos)):
    notas = alunos[n][1]
    media = (notas[0] + notas[1]) / 2
    print(n, alunos[n][0], f'{media:.2f}')

opcao = 0
while opcao != 999:
    print('------------------')
    opcao = int(input('Mostrar notas de qual aluno(a)? [use 999 para sair]: '))
    if opcao == 999:
        print('---- Saindo ----')
    elif 0 <= opcao < len(alunos):
        print('As notas de', alunos[opcao][0], "são", alunos[opcao][1])
    else:
        print('Aluno não encontrado.')