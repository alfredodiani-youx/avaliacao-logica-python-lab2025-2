nome = str(input('Digite o nome:'))
idade = int(input('Digita a idade: '))
nota_media = float(input('Digite a média: '))
idadeDaqui100Anos = 100 - idade

print('-*' *20)
print(f' Olá {nome}!,\n você está com {idade} anos atualmente e faltam {idadeDaqui100Anos} anos para você chegar nos 100 anos de idade.')
if nota_media>= 7:
    print(' Você passou !')
else: 
    print(' Você não passou !')