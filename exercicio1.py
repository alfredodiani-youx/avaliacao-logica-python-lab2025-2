# dados
print('=' * 45)
nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))
media = (float(input('Qual a sua média na escola? ')))
print('=' * 45)

# ate cem anos
ateCem = 100 -idade

# acima ou abaixo da média
if media >= 7:
    print('Você está acima da média!')
else:
    print('Você está abaixo da média!')
print('=' * 45)