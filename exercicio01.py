nome=str(input('Digite o seu nome: ')) #variável que recebe o nome do usuário
idade=int(input('Digite sua idade: ')) #variável que recebe a idade do usuário
notasMedia=float(input('Digite a média de sua nota')) #variável que recebe a média do usuário
anos=100-idade #váriavel que calcula em quantos anos a pessoa terá 100 anos
print(f'{nome}, sua idade é {idade} e daqui {anos} anos você terá 100 anos.') #print formatado com os dados
if notasMedia >= 7.0: #estrutura condicional que atribui condições quando a média for maior ou menor que 7
    print(f'Sua média está acima da média da turma!')
else:
    print(f'Sua média está menor que a média da turma! ')