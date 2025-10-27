# Função para analisar o aluno
def analisar_aluno(nome, notas):
	media = sum(notas) / len(notas)
	situacao = "Aprovado" if media >= 7 else "Reprovado"
	return {"nome": nome, "media": media, "situacao": situacao}

# Programa principal
if __name__ == "__main__":
	alunos = []
	for a in range(3):
		nome = input(f"Nome do aluno {a+1}: ")
		notas = []
		for n in range(3):
			nota = float(input(f"Nota {n+1} de {nome}: "))
			notas.append(nota)
		aluno = analisar_aluno(nome, notas)
		alunos.append(aluno)
	print("\nRelatório de alunos:")
	for aluno in alunos:
		print(f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}, Situação: {aluno['situacao']}")