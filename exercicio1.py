nome = input('Digite seu nome: ')
while True:
    idade = int(input('Digite sua idade: '))
    if idade < 0:
        print('Idade não pode ser negativa. Tente novamente.')
    else:
        break
while True:
    nota_media = float(input('Digite sua nota média: '))
    if nota_media < 0:
        print('A nota não pode ser negativa. Tente novamente.')
    else:
        break
anos_para_100 = 100 - idade
if nota_media >= 7.0:
    status = 'acima da média da turma'
else:
    status = 'abaixo da média da turma'
print('\n===== INFORMAÇÕES DO USUÁRIO =====')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Daqui a {anos_para_100} anos você terá 100 anos!')
print(f'Sua nota média é {nota_media:.1f}, portanto está {status}.')