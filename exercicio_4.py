# Função para analisar o aluno
def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)
    
    if media >= 7:
        situacao = "Aprovado"
    elif 5 <= media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    return {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

# Programa principal
alunos = []

for i in range(3):
    print(f"\n--- Cadastro do {i+1}º aluno ---")
    nome = input("Nome: ")
    
    notas = []
    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        notas.append(nota)
    
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)

# Relatório formatado
print("\n===== RELATÓRIO FINAL =====")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
    print("---------------------------")

'''
O programa principal se inicia já pedindo nome e 3 notas que serão aplicados na função
A função vai utilizar as variáveis notas soma-lás e dividi-lás para obter-nos a média do aluno e verificar a situação, e logo retorna as váriavel Nome, Média e Situação a variável 'aluno'
E adiciona ao 'alunos' os dados da variável 'aluno'
E que no final mostra os dados de cada aluno individualmente e formatado

Observação tentei deixar o código um pouquinho mais bonito
'''