dado_de_aluno = []
lista_de_alunos = []
resposta = ""
print("-="*20)
print("FALE SUAS NOTAS PRA DESCOBRIR SUA MEDIA")
print("-="*20)
while resposta != "n":
    nome = str(input("digite seu nome: "))
    nota1 = int(input("digite sua primeira nota: ")) 
    nota2 = int(input("digite sua segunda nota: "))
    dado_de_aluno.append(nome)
    dado_de_aluno.append(nota1)
    dado_de_aluno.append(nota2)

    lista_de_alunos.append(dado_de_aluno.copy())
    dado_de_aluno.clear() 

    resposta = str(input("quer continuar s ou n : ")).lower()
    while resposta != "s" and resposta != "n":
        resposta = str(input("quer continuar s ou n : ")).lower()
print("-="*20)
print("BOLETIM DOS ALUNOS")
print("-="*20)
for dado_de_aluno in lista_de_alunos:
    media = (dado_de_aluno[1] + dado_de_aluno[2]) / 2
    print(f"nome do aluno: {dado_de_aluno[0]} sua media e {media}")
print("-="*20)
print("NOTAS DO ALUNO ESCOLHIDO:")    
print("-="*20)
while True:
    opçao = int(input("mostras notas de qual aluno? "))
    if opçao == 999:
        break
    if 0 <= opçao <len(lista_de_alunos):
        aluno = lista_de_alunos[opçao]
        print(f"o aluno {dado_de_aluno[0]} tirou {dado_de_aluno[1]} na sua primeira nota e {dado_de_aluno[2]} em sua segunda nota")