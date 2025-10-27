lista = []

while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite sua nota: '))
    nota2 = float(input('Digite sua segunda nota: '))

    media = (nota1 + nota2) / 2 #esse e o calculo da media 

    lista.append([nome, [nota1, nota2], media])

    resposta = str(input('Quer adicionar mais um aluno? (S/N): ')).upper()
    if resposta == 'N':
        break
for aluno in lista:
    print(f"O aluno(a) {aluno[0]} teve as notas {aluno[1]} e média {aluno[2]:.2f}")
print(lista)