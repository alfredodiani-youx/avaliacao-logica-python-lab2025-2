tarefas = []

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada com sucesso.")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i + 1} - {tarefa['titulo']}")

def marcar_concluida():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    
    indice = int(input("Número da tarefa concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída.")
    else:
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    
    indice = int(input("Número da tarefa para remover: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa removida.")
    else:
        print("Número inválido.")

def menu():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()