
tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    tarefa = {"nome": nome, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada!\n")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. {tarefa['nome']} - {status}")
        print()

def marcar_concluida():
    listar_tarefas()
    if len(tarefas) > 0:
        num = int(input("Número da tarefa concluída: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["concluida"] = True
            print("Tarefa marcada como concluída!\n")
        else:
            print("Número inválido.\n")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        num = int(input("Número da tarefa para remover: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas.pop(num)
            print("Tarefa removida!\n")
        else:
            print("Número inválido.\n")

def menu():
    while True:
        print("===== MENU =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar como concluída")
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
            print("Saindo... valeu, parça! 👋")
            break
        else:
            print("Opção inválida!\n")
menu()