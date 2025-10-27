nome=str(input('Digite o seu nome: '))
idade=int(input('Digite sua idade: '))
notasMedia=float(input('Digite a média de sua nota'))
anos=100-idade
print(f'{nome}, sua idade é {idade} e daqui {anos} anos você terá 100 anos.')
if notasMedia >= 7.0:
    print(f'Sua média está acima da média da turma!')
else:
    print(f'Sua média está menor que a média da turma! ')