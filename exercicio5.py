tarefas = []

def adicionar_tarefa():
    titulo = input("Título da tarefa: ")
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        print("Tarefa adicionada!")
    else:
        print("Título não pode ser vazio.")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa ainda.")
    else:
        print("\nTarefas:")
        for i, t in enumerate(tarefas):
            status = "[x]" if t["concluida"] else "[ ]"
            print(f"{status} {i+1} - {t['titulo']}")
    print()

def marcar_concluida():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    num = int(input("Número da tarefa para marcar como concluída: "))
    if num > 0 and num <= len(tarefas):
        tarefas[num-1]["concluida"] = True
        print("Tarefa concluída!")
    else:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    num = int(input("Número da tarefa para remover: "))
    if num > 0 and num <= len(tarefas):
        removida = tarefas.pop(num-1)
        print(f"Tarefa '{removida['titulo']}' removida.")
    else:
        print("Número inválido.")

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        adicionar_tarefa()
    elif op == "2":
        listar_tarefas()
    elif op == "3":
        marcar_concluida()
    elif op == "4":
        remover_tarefa()
    elif op == "5":
    
        break
    else:
        print("Opção inválida, tente de novo.")
