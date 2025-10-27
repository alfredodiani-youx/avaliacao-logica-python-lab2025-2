
resposta = 'S'
alunos = []
lista_nomes = []
lista_notas = []

while resposta != 'N':
    lista_nomes.clear
    nomes = str(input("Qual o seu nome?: "))
    alunos.append(nomes)
    lista_notas.clear()
    resposta_nota = "S"
    while resposta_nota == "S":
        nota = float(input(f"Qual a nota de {nomes}?: "))
        lista_notas.append(nota)
        adicao_nota = str(input('Deseja adicionar mais notas [S/N?]: ')).upper()

    alunos.append(lista_notas)
    lista_nomes.append(alunos.copy())
    pergunta = str(input('Deseja continuar [S/N]?: ')).upper()
    
print(" ")
print(alunos)

for pesquisa, dados in enumerate(alunos):
    print(f"{pesquisa}{dados}{dados}")
while True:
    opcao = str(input("Qual alunos deseja ver? [Digite fim para finalizar o codígo]: "))
    if opcao == "fim":
        print("Finalizado")
        break
    opcao = int(opcao)
    if opcao <= len(alunos) -1:
        print(f"As notas de {alunos[opcao][0]} são {alunos[opcao][1]}")