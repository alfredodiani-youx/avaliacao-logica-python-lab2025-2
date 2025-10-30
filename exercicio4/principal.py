

from funcoes import analisar_aluno  # importa a função do outro arquivo

alunos = []  


for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    notas = [nota1, nota2]
    
    
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)


for a in alunos:
    print(f"Nome: {a['nome']:<10}  Média: {a['media']:.1f}  Situação: {a['situacao']}")