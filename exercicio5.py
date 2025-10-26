tarefas = []

while True:
    print('1- Adicionar tarefa')
    print('2- Listar tarefas')
    print('3- Marcar como concluída')
    print('4- Remover tarefa')
    print('5- Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Qual tarefa você deseja adicionar? ')
        tarefas.append({'titulo': nome, 'concluida': False})

    elif opcao == '2':
        for i in range(len(tarefas)):
            if tarefas[i]['concluida']:
                status = '[x]'
            else:
                status = '[ ]'
            print(f'{i+1} - {status} {tarefas[i]["titulo"]}')

    elif opcao == '3':
        num = int(input('Qual tarefa você deseja marcar como concluida?: ')) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]['concluida'] = True

    elif opcao == '4':
        num = int(input('Qual tarefa você deseja remover? ')) - 1
        if 0 <= num < len(tarefas):
            tarefas.pop(num)

    elif opcao == '5':
        break

    else:
        print('Opção inválida, digite uma opção de 1 a 5...')