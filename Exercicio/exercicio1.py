nome = str(input('Digite deu nome: '))
idade = int(input('Digite sua idade: '))
media = float(input('Digite a sua media de nota: '))
idade_para_100_anos = 100 - idade


print ()
print(f'--'*30)
print(f'Olá, {nome}')
print (f'Sua idade atual é {idade} anos, faltam {idade_para_100_anos} para você completar 100 anos de idade')
if idade >= 7 :
    print (f'PARABÉNS!! Sua nota está acima da media :)')
else :
    print (f'Infelizmente sua nota está abaixo da media :(')