nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
media = float(input('Digite sua média: '))

print('-' * 23)
usuárioCemAnos = 100 - idade
print(f'Para você fazer 100 anos, faltam {usuárioCemAnos} anos.')

if media >= 7:
    print(f'Sua média ({media}), é maior que 7, você está Aprovado!')

else:
    print(f'Sua média é ({media}), é menor que 7, você está Reprovado!')