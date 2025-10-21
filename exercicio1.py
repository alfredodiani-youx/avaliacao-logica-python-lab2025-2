

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota média: "))


anos = 100 - idade


if nota >= 7:
    situacao = "acima da média da turma"
else:
    situacao = "abaixo da média da turma"


print(f"Olá, {nome}!")
print(f"Você tem {idade} anos e sua nota média é {nota}.")
print(f"Sua nota está {situacao}.")
print(f"Você terá 100 anos daqui a {anos} anos.")