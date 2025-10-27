listaTarefas = []

def novaTarefa(listaTarefas):
    print('-' * 30)
    nomeTarefa = str(input('Digite o nome da tarefa: '))
    print('Tarefa criada.')

    listaTarefas.append({"nome": nomeTarefa, "concluida": False})

def listarTarefas(listaTarefas):
    if len(listaTarefas) == 0:
        print('-' * 30)
        print('Você não tem nenhuma tarefa.')

    else:
        print('-' * 30)
        print('Sua lista de Tarefas:\n')

        for indice, tarefa in enumerate(listaTarefas):
            if tarefa["concluida"] == True:
                print(f'[x] {indice + 1} - {tarefa["nome"]}')

            else:
                print(f'[ ] {indice + 1} - {tarefa["nome"]}')

    print('-' * 30)

def marcarConcluido(listaTarefas):
    listarTarefas(listaTarefas)
    escolhaMarcar = int(input('Qual tarefa você quer marcar como concluída? ')) - 1

    try:
        if 0 <= escolhaMarcar < len(listaTarefas):
            listaTarefas[escolhaMarcar]['concluida'] = True
            print('Tarefa concluída')
        else:
            print('ERRO! Essa tarefa não existe na lista!')

    except ValueError:
        print('Essa resposta não é Válida.')

def removerTarefa(listaTarefas):
    listarTarefas(listaTarefas)
    escolhaRemover = int(input('Qual tarefa você quer remover? ')) - 1

    try:
        if 0 <= escolhaRemover < len(listaTarefas):
            del listaTarefas[escolhaRemover]
            print('Tarefa removida.')
        else:
            print('ERRO! Essa tarefa não existe na lista!')

    except ValueError:
        print('Essa resposta não é Válida.')

def menuTarefas():
    while True:
        print('-' * 30)
        print(f'[ 1 ] - Adicionar Tarefa')
        print(f'[ 2 ] - Listar Tarefas')
        print(f'[ 3 ] - Marcar Concluída')
        print(f'[ 4 ] - Remover Tarefa')
        print(f'[ 5 ] - Sair')
        print('-' * 30)

        escolhaUsuario = int(input(f'Escolha uma das opções: '))

        if escolhaUsuario == 1:
            novaTarefa(listaTarefas)

        elif escolhaUsuario == 2:
            listarTarefas(listaTarefas)

        elif escolhaUsuario == 3:
            marcarConcluido(listaTarefas)

        elif escolhaUsuario == 4:
            removerTarefa(listaTarefas)

        elif escolhaUsuario == 5:
            print('Programa encerrado.')
            break

if __name__ == "__main__":
    menuTarefas()