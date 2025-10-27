# ===== GERENCIADOR DE TAREFAS =====

# Lista de tarefas (cada tarefa é um dicionário)
tarefas = []


def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        print(f"Tarefa '{titulo}' adicionada com sucesso!")
    else:
        print("O título da tarefa não pode ser vazio.")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i} - {tarefa['titulo']}")
    print("========================\n")


def marcar_concluida():
    listar_tarefas()
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print(f"Tarefa '{tarefas[indice]['titulo']}' marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida['titulo']}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


def menu():
    while True:
        print("""
===== GERENCIADOR DE TAREFAS =====
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Sair
""")
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
            print("Encerrando o programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


#Início do programa
menu()

'''
tarefas é onde guarda todas a tarefas
adicionar_tarefa() → pede o nome da tarefa e coloca na lista.

listar_tarefas() → mostra todas as tarefas, com [ ] para não concluída e [x] para concluída.

marcar_concluida() → o usuário escolhe o número da tarefa e ela é marcada como feita.

remover_tarefa() → o usuário escolhe o número e a tarefa é apagada.

menu() → mostra o menu principal e chama as funções certas.

Ele só para quando o usuário escolhe “5 – Sair”.
'''