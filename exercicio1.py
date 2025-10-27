nome = input('Nome do aluno: ')
idade = int(input('Sua idade: '))
media = float(input('Digite a média: '))

calculoIdade =  100 - idade

print('-' * 30)
print(f'Sua idade daqui a 100 anos é:{calculoIdade}')
print(f'')

if media >= 7:
    print(f'A média do aluno é maior que 7, então ele esta \033[32mAPROVADO\033[m')

else:
    print(f'A média do aluno é menor que 7, ele esta \033[31mREPROVADO\033[m')