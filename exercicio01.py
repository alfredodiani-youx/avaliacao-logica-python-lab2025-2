# Entrada, Processamento e Saída
# Esse programa pede o nome, idade e a media do úsuario; calcula a média e verifica se se ele(úsuario) está acima ou abaixo da média.



nome = str(input('Qual o seu nome?: '))
idade = int(input('Qual a sua idade?: '))
nota_media = float(input('Qual a sua média?: '))

anos_para_100 = 100 - idade

if nota_media > 7:
    print(" ")
    print('Você está acima da média!')
    print(' ')
else: 
    print(' ')
    print('Você está abaixo da média!')
    print(' ')
    
print(f'''Seu nome é {nome},
sua idade é {idade} anos,
e sua média é {nota_media}
faltam {anos_para_100} anos para você ter 100 anos''')