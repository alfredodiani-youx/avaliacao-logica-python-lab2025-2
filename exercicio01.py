# Entrada, Processamento e Saída

nome = str(input('Qual o seu nome?: '))
idade = float(input('Qual a sua idade?: '))
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
sua idade é {idade},
e sua média é {nota_media}''')