import listar_tarefas
import remover_tarefa
import marcar_concluida
import adicionar_tarefa


tarefas = []
while True:
    print("\n=== MENU DE TAREFAS ===")
    print("1 – Adicionar tarefa")
    print("2 – Listar tarefas")
    print("3 – Marcar tarefa como concluída")
    print("4 – Remover tarefa")
    print("5 – Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa.adiconar(tarefas)
    elif opcao == "2":
        listar_tarefas.listar(tarefas)
    elif opcao == "3":
        marcar_concluida.marcar(tarefas)
    elif opcao == "4":
        remover_tarefa.remover(tarefas)
    elif opcao == "5":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

