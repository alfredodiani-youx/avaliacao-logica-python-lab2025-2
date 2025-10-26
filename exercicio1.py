nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
media_nota = float(input('Qual foi a sua nota média? '))

anos_para_100 = 100 - idade 

if media_nota >= 7:
    media = ('PARABÉNS, sua nota está acima da média da turma! ')
else:
    media = ('sua nota está abaixo da média da turma, ESTUDE MAIS!')


print(f'----- RESULTADO -----')
print(f'Nome: {nome}')
print(f'Idade:{idade} anos')
print(f'Daqui a {anos_para_100} anos, {nome} terá 100 anos!')
print(f'Sua nota média foi {media_nota}.')
print(f'Portanto, {media}')