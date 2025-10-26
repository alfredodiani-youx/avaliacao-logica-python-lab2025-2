print('-'*30)
print('         Cadastro        ')
print('-'*30)
nome=input('Digite o seu nome: ')
idade=int(input('Digite a sua idade: '))
media=float(input('Digite a sua média: '))
print('-'*30)
CEManos= 100
idadeFutura=CEManos-idade
if media >= 7.0:
    print(f'- {nome} tem {idade} anos e terá 100 anos daqui a {idadeFutura} anos. Sua média é {media} e está APROVADO!')
else:
    print(f'- {nome} tem {idade} anos e terá 100 anos daqui a {idadeFutura} anos. Sua média é {media} e está REPROVADO!')


