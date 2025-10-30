def analisar_aluno(nome, notas):
    media = sum(notas) / len(notas) # soma todos valores da lista e divide

    if media >=7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    aluno = {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }
    return aluno