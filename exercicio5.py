def menu():
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, t in enumerate(tarefas, 1):
            status = "[x]" if t["concluida"] else "[ ]"
            print(f"{status} {i} - {t['titulo']}")

def main():
    tarefas = []
    while True:
        menu()
        op = input("Escolha: ")

        if op == "1":
            titulo = input("Título da tarefa: ").strip()
            if titulo:
                tarefas.append({"titulo": titulo, "concluida": False})
                print("Tarefa adicionada!")
            else:
                print("Título não pode ser vazio.")
        elif op == "2":
            listar(tarefas)
        elif op == "3":
            listar(tarefas)
            if tarefas:
                try:
                    i = int(input("Número da tarefa: ")) - 1
                    tarefas[i]["concluida"] = True
                    print("Tarefa concluída!")
                except:
                    print("Entrada inválida.!")
        elif op == "4":
            listar(tarefas)
            if tarefas:
                try:
                    i = int(input("Número da tarefa: ")) - 1
                    print(f"Tarefa '{tarefas.pop(i)['titulo']}' removida.")
                except:
                    print("Entrada inválida.!")
        elif op == "5":
            break
        else:
            print("Opção inválida.!")

if __name__ == "__main__":
    main()

