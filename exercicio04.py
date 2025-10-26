def analisar_aluno(nome, notas):
    media = (notas[0] + notas[1] + notas[2])

    if media >= 7:
        situacao = "Foi aprovado !"
    else:
        situacao = "Foi reprovado 1"

    return {"nome": nome, "media": media, "situacao": situacao}

alunos = []

for c in range(3):
    print(f"--- Cadastro do {c+1}º aluno ---")
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    notas = [n1, n2, n3]
    aluno = analisar_aluno(nome, notas)
    alunos.append(aluno)

print('------------- Notas finais -------------')
for a in alunos:
    print(f"Aluno: {a['nome']}")
    print(f"Média: {a['media']:.1f}")
    print(f"Situação: {a['situacao']}")
    print("---------------------------")