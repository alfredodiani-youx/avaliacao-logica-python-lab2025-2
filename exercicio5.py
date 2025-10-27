tarefas = []

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    """Exibe todas as tarefas, mostrando seu status."""
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\nLista de Tarefas")
    for i, tarefa in enumerate(tarefas, 1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i} - {tarefa['titulo']}")
    print("-\n")

def marcar_tarefa_concluida():
    """Marca uma tarefa como concluída com base no seu número."""
    listar_tarefas()
    try:
        num_tarefa = int(input("Digite o número da tarefa para marcar como concluída: "))
        if 1 <= num_tarefa <= len(tarefas):
            tarefas[num_tarefa - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def remover_tarefa():
    """Remove uma tarefa da lista com base no seu número."""
    listar_tarefas()
    try:
        num_tarefa = int(input("Digite o número da tarefa para remover: "))
        if 1 <= num_tarefa <= len(tarefas):
            tarefas.pop(num_tarefa - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def menu():
    """Exibe o menu interativo e processa a escolha do usuário."""
    while True:
        print("Sistema de Tarefas")
        print("1 – Adicionar tarefa")
        print("2 – Listar tarefas")
        print("3 – Marcar tarefa como concluída")
        print("4 – Remover tarefa")
        print("5 – Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                marcar_tarefa_concluida()
            elif opcao == 4:
                remover_tarefa()
            elif opcao == 5:
                print("Finalizando sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Digite um número.")

if __name__== "__main__":
    menu()
