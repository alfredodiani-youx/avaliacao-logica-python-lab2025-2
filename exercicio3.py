lista = []
while True:
    print('=' * 30)
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite a nota 1 do aluno: '))
    nota2 = int(input('Digite a nota 2 do aluno: '))
    media = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], media])
    print('=' * 30)
    resposta = str(input('Quer continuar? [S/N]')).strip()[0]
    if resposta in 'Nn':
        print()
        print('<finalizando...>')
        print()
        break
print('=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('=' * 30)
    opc = int(input('Mostrar notas de qual aluno? [999 para interromper]'))
    if opc == 999:
        print('=' * 30)
        break
    elif opc <= len(lista)-1:
        print('=' * 30)
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
