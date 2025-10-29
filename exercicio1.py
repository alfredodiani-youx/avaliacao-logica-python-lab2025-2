print('-'*60)
print('\033[34m                       Cadastro                      \033[m')
print('-'*60)
nome = input('Digite o seu nome: ').capitalize()
idade = int(input('Digite a sua idade: '))
media = float(input('Digite a sua média: '))
print('-'*60)
CEManos = 100
idadeFutura = CEManos - idade
if media >= 7.0:
    print(f'- {nome} tem {idade} anos e terá 100 anos daqui a {idadeFutura} anos.\n- A média de {nome} é {media} e está \033[32mAPROVADO!\033[m')
else:
    print(f'- {nome} tem {idade} anos e terá 100 anos daqui a {idadeFutura} anos.\n- A média de {nome} é {media} e está \033[31mREPROVADO!\033[m')


