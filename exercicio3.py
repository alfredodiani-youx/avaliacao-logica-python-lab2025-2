listaAlunos = []
lista_nomes = []
lista_notas = []
resposta = 'S'

while resposta != 'N':
    lista_nomes.clear
    nomes = str(input("Qual o seu nome: "))
    listaAlunos.append(nomes)

    while resposta != "N":    
        lista_notas.clear()
        nota = float(input(f"Qual a nota de {nomes}: "))
        lista_notas.append(nota)
        listaAlunos.append(lista_notas)
        lista_nomes.append(listaAlunos.copy())
        resposta = str(input('Deseja continuar [S/N]?: ')).upper()    
print(listaAlunos)

for pesquisa, dados in enumerate(listaAlunos):

    print(f"{pesquisa}{dados}{dados}")

while True:
    opcao = str(input("Qual alunos deseja ver? [Digite fim para finalizar o codígo]: "))

    if opcao == "fim":
        print("Finalizado")

        break

    opcao = int(opcao)

    if opcao <= len(listaAlunos) -1:
        print(f"As notas de {listaAlunos[opcao][0]} são {listaAlunos[opcao][1]}")