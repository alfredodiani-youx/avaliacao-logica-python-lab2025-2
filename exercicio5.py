# Gerenciador de Tarefas simples

tarefas = []

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo == "":
        print("Título não pode ser vazio.")
        return
    tarefa = {"titulo": titulo, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nTarefas:")
    for i, t in enumerate(tarefas, start=1):
        status = "[x]" if t["concluida"] else "[ ]"
        print(f"{status} {i} - {t['titulo']}")
    print()

def marcar_concluida():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    try:
        num = int(input("Número da tarefa para concluir: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) == 0:
        return
    try:
        num = int(input("Número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

# Programa principal
while True:
    print("""
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar como concluída
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
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

