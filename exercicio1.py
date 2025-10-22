nome=str(input('Digite o nome: '))
idade=int(input('Digite a idade: '))
notaMedia=float(input('Digite a nota: '))


tempo = 100 - idade
if notaMedia > 7:
    print('A nota é maior que a media')
else:
    print('A nota é menor que a media')


print(f"O nome é {nome}")
print(f'A idade é {idade} e falta {tempo} anos pra ele fazer 100 anos ')