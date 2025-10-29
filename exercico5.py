def menu():
    print('\n\033[33mMENU DE TAREFA\033[m')
    print('1- adicionar tarefas\n'+
          '2- lista tarefas\n'+
          '3- marcar tarefas como concluida\n'+
          '4- remover tarefas\n'+
          '5- sair\n'
          )
    
def lista_tarefas():
    for indice, tarefas in enumerate(tarefas):
        if tarefa['concluindo'] == True:
            tarefa_concluida = 'x'
        else:
            tarefa_concluida = ' '
        print(f'[{tarefa_concluida}] {indice} - {tarefa["titulo"]}')

tarefa = []

while True:
    menu()
    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        titulo = input('Digite a tarefa: ')
        tarefa.append({'Titulo': titulo, 'Concluida': False})

    if opcao == '2':
       lista_tarefas()

    if opcao == '3':
        lista_tarefas()
        lista_marcar = int(input('Qual indice da tarefa voce deseja marcar? '))
        tarefa[lista_marcar]['concluida'] = True

        # lista_tarefas()
        # lista_remover = int(input('Qual tarefa deseja remover? '))


        # tarefa = []
        # if len(tarefa) == 0:
        #     print("Não há tarefas para remover")
        # else:
        #     print("Qual tarefa deseja remover? ")

            #Como remover por índice em uma lista
    if opcao == '4':
        lista_tarefas()
        if tarefa:
            try:
                lista_remover = int(input("Qual o índice da tarefa que deseja remover? "))
                if 0 <= lista_remover < len(tarefa):
                    del tarefa[lista_remover]
                    print("Tarefa removida com sucesso!\n")
                else:
                    print("Índice inválido.\n")
            except ValueError:
                print("Por favor, insira um número válido para o índice.\n")
    elif opcao == '5':
        print("Saindo do programa. Até mais!")
    
        break
    if opcao == '5':
        break

    
