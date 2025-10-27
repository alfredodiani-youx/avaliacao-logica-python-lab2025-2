# cadastra o aluno e os seus dados
def cadastrar():
    alunos = []
    print('Vamos cadastrar os alunos! (deixe o nome vazio pra parar)')
    while True:
        nome = input('Nome do aluno: ').strip()
        if nome == '':
            break
        try:
            nota1 = float(input(f'Nota 1 de {nome}: '))
            nota2 = float(input(f'Nota 2 de {nome}: '))
        except Exception:
            print('Nota inválida, vamos pular esse aluno. Tenta de novo se quiser.')
            continue
        alunos.append([nome, [nota1, nota2]])
    return alunos

# mostra o boletim formatatado
def mostrar_boletim(alunos):
    print('\n=== BOLETIM ===')
    if not alunos:
        print('Sem alunos aqui :(')
        return
    for i, (nome, notas) in enumerate(alunos):
        media = (notas[0] + notas[1]) / 2
        print(f'{i} - {nome} -> média: {media:.2f}')


def ver_notas(alunos, indice):
    return alunos[indice][1]


def main():
    alunos = cadastrar()
    mostrar_boletim(alunos)
    while True:
        escolha = input("Quer ver as notas de qual índice? (digite 'sair' pra fechar): ").strip()
        if escolha.lower() in ('sair', 's'):
            print('Tchau, valeu!')
            break
        if not escolha.isdigit():
            print('Coloca um número aí, por favor...')
            continue
        index = int(escolha)
        if 0 <= index < len(alunos):
            nome = alunos[index][0]
            notas = ver_notas(alunos, index)
            print(f'Notas do {nome}: {notas}')
        else:
            print('Índice inválido, tenta outro.')


if __name__ == '__main__':
    main()
