alunos = []  

while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    alunos.append([nome, [nota1, nota2]])

    resposta = str(input('Você quer se cadastrar novamente? (S/N) ')).upper()
    if resposta == 'N':
        break


for i, a in enumerate(alunos):
    media = (a[1][0] + a[1][1]) / 2         #calculando a média dos alunos
    print(f'{i:<4}{a[0]:<15}{media:>8.1f}')


while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:            # opcão de finalizar
        print('finalizando.')
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')    # escolher qual nota especifica para mostrar
