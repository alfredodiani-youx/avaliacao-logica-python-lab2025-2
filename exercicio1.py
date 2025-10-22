nome = input('Qual seu nome?')
idade = float(input('Qual sua idade?'))
daqui100 = idade - 100
nota = float(input('Qual a média da turma?'))
if nota >= 7.0:
    print('Parabens, você esta acima da média.')
else :
        print('Você está abaixo da média,estude mais.')
print(f'Só uma curiosidade,daqui {daqui100} você tera 100 anos')



print('-=' *18)
print(f'   seu nome é {nome}')
print('-' *35)
print(f'   Você tem {idade} anos')
print('-' *35)
print(f'   daqui {daqui100} você tera 100 anos')
print('-' *35)
print(f'   e média da turma foi de {nota}')
print('-=' *18)