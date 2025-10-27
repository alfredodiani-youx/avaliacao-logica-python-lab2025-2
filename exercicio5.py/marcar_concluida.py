import listar_tarefas


def marcar(tarefas):
    listar_tarefas.listar(tarefas)
    if not tarefas:
        return
    try:
        indice =int(input('Número da tarefas para marcar concluida: '))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["concluida"] = True
            print(f"Tarefa '{tarefas[indice - 1]['titulo']}' marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")