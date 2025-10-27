
idade = int(input("Digite sua idade: "))
nome = str(input('Digite seu nome: '))
nota = float(input('Digite sua nota: '))

ano = 100 - idade
if nota >= 7.0:
    print('Sua nota está na media')
else:
    print('Sua nota está a baixo da madia')

print(f"Voce tera 100 anos daqui há {ano}")