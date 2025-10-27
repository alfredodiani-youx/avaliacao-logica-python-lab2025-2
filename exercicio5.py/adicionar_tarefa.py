def adiconar (tarefas):
    titulo = input("Digite o titulo da tarefa: ")
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        print (f"Tarefa '{titulo}'adicionada ")
    else:
        print("Titulo invalido, tente de novo")

        