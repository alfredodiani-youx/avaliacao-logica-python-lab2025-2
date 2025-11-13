def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        print("✅ Tarefa adicionada com sucesso!")
    else:
        print(" Título inválido!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return
    print("\n=== LISTA DE TAREFAS ===")
    for i, tarefa in enumerate(tarefas, 1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i} - {tarefa['titulo']}")
    print("=========================")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa a marcar como concluída: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            print("✅ Tarefa marcada como concluída!")
        else:
            print(" Número inválido!")
    except ValueError:
        print(" Digite um número válido!")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            print(f"🗑️ Tarefa '{removida['titulo']}' removida!")
        else:
            print(" Número inválido!")
    except ValueError:
        print(" Digite um número válido!")

def menu():
    tarefas = []
    while True:
        print("""
=== MENU DE TAREFAS ===
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print(" Saindo do sistema. Até logo!")
            break
        else:
            print(" Opção inválida! Tente novamente.")
menu()