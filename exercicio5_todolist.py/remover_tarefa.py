import listar_tarefas


def remover(tarefas):
    listar_tarefas.listar(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Número da tarefa a remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{removida['titulo']}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

