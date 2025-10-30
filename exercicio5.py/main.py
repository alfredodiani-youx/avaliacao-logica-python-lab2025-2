
from funcoes import adicionar_tarefa, mostrar_tarefas, concluir_tarefa, remover_tarefa

def mostrar_menu():
    print("Tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Mostrar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

def iniciar_programa():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            mostrar_tarefas()
        elif escolha == "3":
            concluir_tarefa()
        elif escolha == "4":
            remover_tarefa()
        elif escolha == "5":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida, Tente novamente.")


