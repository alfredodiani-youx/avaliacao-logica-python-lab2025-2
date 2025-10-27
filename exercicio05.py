tarefas = []

def adicionar_tarefa():
    nomeTarefa = input("Digite o nome da tarefa: ")
    tarefa = {"titulo": nomeTarefa, "concluida": False}
    tarefas.append(tarefa)
    print("Essa tarefa foi adicionada a lista !!")


def listar_tarefas():
    if not tarefas:
        print("Não tem tarefas cadastradas.")
    else:
        print("--- L i s t a  d e  t a r e f a s ---")
        for i, t in enumerate(tarefas, 1):
            status = "[x]" if t["concluida"] else "[ ]"
            print(f"{status} {i} - {t['titulo']}")
        print("------------------------\n")


def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        num = int(input("Digite o número da tarefa concluída: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            print("Tarefa concluída!\n")
        else:
            print("Número inválido!\n")


def remover_tarefa():
    listar_tarefas()
    if tarefas:
        num = int(input("Número da tarefa que deseja remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Essa tarefa foi removida!\n")
        else:
            print("Número inválido!\n")

while True:
    print("- - - -  T a r e f a s - - - -")
    print("1º - Adicionar tarefa")
    print("2º - Listar tarefas")
    print("3º - Marcar como concluída")
    print("4º - Remover tarefa")
    print("5º - Sair")

    escolha = input("Escolha uma das opções: ")
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        concluir_tarefa()
    elif escolha == "4":
        remover_tarefa()
    elif escolha == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!\n")