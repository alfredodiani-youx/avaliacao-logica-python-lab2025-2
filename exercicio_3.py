listaDeAlunos = []
aluno = []
notas = []
numeroDoAluno = 0
quantidadeAluno = int(input('Escolha a quantidade de alunos: '))

for c in range (quantidadeAluno):
    nome = input('Coloque o nome do aluno: ')
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    listaDeAlunos.append(aluno[:])
    notas.clear()
    aluno.clear()

for i in listaDeAlunos:
    print(f'Os alunos escolhidos foram : {i[0]}\nE sua médias de notas foram respectivamente:\n{(i[1][0]+i[1][1])/2}')
    
opcao = input('Você gostaria ver as notas individuais de algum aluno?\nSe sim digite S ou s: ').strip().upper()
counter = 0

while opcao == 'S':
    for p in listaDeAlunos:
        print(f'{p[0]} -> {counter}')
        counter += 1
    escolha = int(input('Qual aluno você gostaria de ver as notas?'))
    print(listaDeAlunos[escolha][1])
    opcao = input('Você gostaria de continuar?\nSe sim, digite S ou s: ').strip().upper()

print = ('Fim')

'''
Aqui nós temos 3 listas: 1 para as notas, 1 para os dados dos alunos (nome e notas) e 1 para guardar todos os alunos
Primeiro criei um sistema que eu seleciono o número de alunos que quero avaliar,
Logo em seguida peço as informações nome do aluno e coloco na lista 'aluno', nota1 e nota2 que serão adicionadas a lista 'notas' e faço copy dessas informações e clear para limpar as listas e não criar informações repetidas
Depois o programa escreve o nome de cada aluno e sua média de notas e da opção de escolher se você quer ver todas as informações individuais dos alunos ou não
E ele vai mostrar o nome do aluno e suas notas inviduais que você escolher, ou seja, nota1 e nota2 respectivamente 
'''