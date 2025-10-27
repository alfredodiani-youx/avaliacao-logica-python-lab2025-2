def listar(tarefas):
    if not tarefas:
        print (f'Nenhuma tarefa')
    else:
        print("\n=== LISTA DE TAREFAS ===")
        for i, t in enumerate(tarefas, start=1):
            status = "[x]" if t["concluida"] else "[ ]"
            print(f"{status} {i} - {t['titulo']}")
        print()