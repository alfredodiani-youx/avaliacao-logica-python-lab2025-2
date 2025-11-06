def adicionar(tarefas):
    titulo = input('Título da tarefa: ')
    tarefas.append({'titulo': titulo, 'concluida': False})
    print('Tarefa adicionada!')


def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa cadastrada.\n')
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = '[x]' if tarefa['concluida'] else '[ ]'
            print(f'{status} {i} - {tarefa["titulo"]}')
        print()


def concluir(tarefas):
    listar(tarefas)
    if tarefas:
        num = input('Número da tarefa concluída: ')
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(tarefas):
                tarefas[num - 1]['concluida'] = True
                print('Tarefa marcada como concluída!')
            else:
                print('Número fora do intervalo!')
        else:
            print('Entrada inválida! Digite um número.')


def remover(tarefas):
    listar(tarefas)
    if tarefas:
        num = input('Número da tarefa para remover: ')
        if num.isdigit():
            num = int(num)
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                print(f'Tarefa "{removida["titulo"]}" removida!')
            else:
                print('Número fora do intervalo!')
        else:
            print('Entrada inválida! Digite um número.')


def menu():
    tarefas = []
    while True:
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Marcar como concluída')
        print('4 - Remover tarefa')
        print('5 - Sair')
        opcao = input('Escolha: ')
        print()

        if opcao == '1':
            adicionar(tarefas)
        elif opcao == '2':
            listar(tarefas)
        elif opcao == '3':
            concluir(tarefas)
        elif opcao == '4':
            remover(tarefas)
        elif opcao == '5':
            print('Encerrando... até logo!')
            break
        else:
            print('Opção inválida.\n')


menu()