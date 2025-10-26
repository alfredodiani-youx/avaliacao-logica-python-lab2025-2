nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
media = float(input('Digite sua nota média: '))


anos_100 = 100 - idade
media_acima = media >= 7.0

print('--- RESULTADO ---')
print(f'Olá, {nome}')
print(f'Você terá 100 anos em {anos_100} anos')

if media_acima:
    print('Sua media está acima da media da turma! ')
else:
    print('Sua media está abaixo da media da turma. ')