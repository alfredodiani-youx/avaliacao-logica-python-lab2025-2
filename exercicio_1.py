# Programa: Informações do Usuário

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota_media = float(input("Digite sua nota média: "))

# Processamento
anos_para_100 = 100 - idade

# Verificando se a nota é acima da média
if nota_media >= 7.0:
    situacao = "acima ou igual à média da turma"
else:
    situacao = "abaixo da média da turma"

# Saída formatada
print(f'--- Informações ---')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Nota média: {nota_media:.2f}')

if anos_para_100 == 0:
    print('Parabéns! Você tem 100 anos!')
elif anos_para_100 < 0:
    print('Parabéns! Você tem mais de 100 anos!')
else:
    print(f'Daqui a {anos_para_100} anos, você terá 100 anos')

print(f'Sua nota está {situacao}.')