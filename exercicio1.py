nome = str(input('>> Nome: '))
idade = int(input('>> Idade: '))
notaMedia = float(input('>> Média: '))
idadeMais100Anos = 100 - idade
print('-'*15)
print(f'-Nome: {nome}\n-Idade: {idade}\n-Você terá 100 anos daqui: {idadeMais100Anos} anos\n-Situação: {notaMedia}')
if notaMedia >= 7.0:
    print('-'*15)
    print('-> Você foi APROVADO!')
else:
    print('-'*15)
    print('-> Você foi REPROVADO!')