def menu():
    print('\n---\033[33mMenu de tarefas\033[m--')
    print("1- Adicionar tarefas\n" +
          "2- Lista tarefas\n" +
          "3- Marcar tarefas como concluida\n" +
          "4- Removar tarefas\n" +
          "5- Sair\n" 
          )

def listar_tarefas():
    for indice, tarefa in enumerate(tarefas): # dentro de tarefas enumeradas
            if tarefa['concluida'] == True:
                tarefa_concluida = 'x'
            else:
                tarefa_concluida = ' '
            print(f'[{tarefa_concluida}] {indice} - {tarefa["titulo"]}') 



tarefas = []

while True:
    menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        titulo = input('Digite a tarefa: ').capitalize()
        tarefas.append({'titulo': titulo, 'concluida': False})
        print('\033[32mTarefa adicionada!\033[m')

    
    if opcao == '2':
        listar_tarefas()

    if opcao == '3':
        listar_tarefas()
        tarefa_marcar = int(input('Qual indice da tarefa você deseja marcar? '))
        tarefas[tarefa_marcar]['concluida'] = True
        print('\033[32mTarefa marcada com sucesso!\033[m')

    if opcao == '4':
        listar_tarefas()
        if tarefas:
            try:
                lista_remover = int(input("Qual o índice da tarefa que deseja remover? "))
                if 0 <= lista_remover < len(tarefas):
                    del tarefas[lista_remover]
                    print("\033[32mTarefa removida com sucesso!\033[m\n")
                else:
                    print("\033[31mÍndice inválido.\033[m\n")
            except ValueError:
                print("Por favor, insira um número válido para o índice.\n")

    elif opcao == '5':
        print("\033[34mSaindo do programa. Até mais!\033[m")
        break
    