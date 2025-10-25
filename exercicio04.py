def analisar_aluno(nome, notas):
     
     media = sum(notas) / len(notas)
     if media >= 7.0:
         situacao = "Aprovado"
     else:
         situacao = "Reprovado"

     return {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

dados = [
    {"nome": "Agatha", "notas": [7.0, 7.5, 8.0]},
    {"nome": "luis", "notas": [5.0, 10.0, 6.5]},
    {"nome": "Emilly", "notas": [3.0, 4.0, 4.5]}
]

relatorios = []

for aluno in dados:
    relatorios.append(analisar_aluno(aluno["nome"], aluno["notas"]))

print("Relatório dos Alunos:")
for relatorio in relatorios:
    print(f"Nome: {relatorio['nome']}")
    print(f"Média: {relatorio['media']:.2f}")
    print(f"Situação: {relatorio['situacao']}")
    print()