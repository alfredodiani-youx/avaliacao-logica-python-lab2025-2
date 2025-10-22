nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
media = float(input("Digite a sua nota média: "))
anospara100 = 100 - idade
if media >= 7.0:
    situacao = "acima da média da turma"
else:
    situacao = "abaixo da média da turma"

print(f"{nome}!")
print(f"Você tem {idade} anos e terá 100 anos daqui a {anospara100} anos.")
print(f"Sua nota média é {media:.2f}, o que significa que está {situacao}.")