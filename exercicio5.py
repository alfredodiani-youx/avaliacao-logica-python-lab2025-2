
tarefas = []

while True:
    print("\n=== MENU DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título da tarefa: ")
        tarefa = {"titulo": titulo, "concluida": False}
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\n--- LISTA DE TAREFAS ---")
            for i in range(len(tarefas)):
                if tarefas[i]["concluida"]:
                    status = "[x]"
                else:
                    status = "[ ]"
                print(f"{status} {i+1} - {tarefas[i]['titulo']}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para marcar.")
        else:
            num = int(input("Digite o número da tarefa: "))
            if num > 0 and num <= len(tarefas):
                tarefas[num-1]["concluida"] = True
                print("Tarefa concluída!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            num = int(input("Digite o número da tarefa: "))
            if num > 0 and num <= len(tarefas):
                removida = tarefas.pop(num-1)
                print(f"Tarefa '{removida['titulo']}' removida!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        print("Saindo... Volte sempre!")
        break

    else:
        print("Opção inválida, tente novamente.")