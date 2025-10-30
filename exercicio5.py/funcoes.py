

tarefas = []  

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    nova_tarefa = {"nome": nome, "concluida": False}
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada")

def mostrar_tarefas():
    if not tarefas:
        print(" Nenhuma tarefa encontrada")
        return
    
    print(" Lista de Tarefas ")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{status} {i}. {tarefa['nome']}")
    print()

def concluir_tarefa():
    mostrar_tarefas()
    if not tarefas:
        return
    
    numero = int(input("Número da tarefa concluída: "))
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print(" Tarefa concluída ")
    else:
        print("Numero inválido.")

def remover_tarefa():
    mostrar_tarefas()
    if not tarefas:
        return
    
    numero = int(input("Numero da tarefa para remover: "))
    if 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print("Tarefa removida")
    else:
        print("Numero inválido")