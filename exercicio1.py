nome = input("Insira o seu nome:")
idade = int(input("Insira a sua idade:"))
notamedia = float(input("Digite a sua nota:"))

tempo = 100 - idade

if notamedia >= 7.0:
    situacao = ("Acima da média!")
else:
    situacao = ("Abaixo da média!")

print("\n===== RESULTADO =====")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Daqui a {tempo} anos, {nome} terá 100 anos!.")
print(f"Sua nota média é {notamedia:1f}, o que está {situacao}.")
