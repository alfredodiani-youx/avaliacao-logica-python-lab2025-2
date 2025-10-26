def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

