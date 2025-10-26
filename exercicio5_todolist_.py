def menu():
    print('-'*30)
    print('''
      MENU PRINCIPAL
          
1 - Adicionar tarefa
2 - Listar tarefas
3 - Marcar tarefa como concluída
4 - Remover tarefa
5 - Sair
''')
    print('-'*30)

def adicionar_tarefas(tarefas):
    tarefa = input('Nome da tarefa: ')
    if tarefa:
        tarefas.append({"titulo": tarefa, "concluida": False})
        print(f'- Tarefa "{tarefa}" adicionada!')
    else:
        print('\033[31mNome da tarefa inválido!\033[m')

def lista_tarefas(tarefas):
    print(' LISTAGEM DE TAREFAS')
    if not tarefas:
        print('\033[31m- Nenhuma tarefa cadastrada!\033[m')
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            status = '[x]' if tarefa["concluida"] else '[ ]'
            print(f'{status} {indice} - {tarefa["titulo"]}')
    print('-'*30)

def marcar_concluida(tarefas):
    lista_tarefas(tarefas)
    if not tarefas:
        return
    try:
        numeroTarefa = int(input('Número da tarefa para marcar como concluída: '))
        if 1 <= numeroTarefa <= len(tarefas):
            tarefa = tarefas[numeroTarefa - 1]
            if tarefa["concluida"]:
                print('Essa tarefa já estava concluída!')
            else:
                tarefa["concluida"] = True
                print(f'Tarefa "{tarefa["titulo"]}" marcada como concluída!')
        else:
            print('\033[31mNúmero inválido!\033[m')
    except ValueError:
        print('\033[31mDigite um número válido!\033[m')

def remover_tarefas(tarefas):
    lista_tarefas(tarefas)
    if not tarefas:
        return
    try:
        numeroTarefa = int(input('Número da tarefa que deseja remover: '))
        if 1 <= numeroTarefa <= len(tarefas):
            removida = tarefas.pop(numeroTarefa - 1)
            print(f'Tarefa "{removida["titulo"]}" removida!')
        else:
            print('\033[31mNúmero inválido!\033[m')
    except ValueError:
        print('\033[31Digite um número válido!\033[m')

def fluxo():
    tarefas = []
    while True:
        menu()
        try:
            escolha = int(input('Escolha: '))
        except ValueError:
            print('\033[31mDigite um número válido!\033[m')
            continue

        if escolha == 1:
            adicionar_tarefas(tarefas)
        elif escolha == 2:
            lista_tarefas(tarefas)
        elif escolha == 3:
            marcar_concluida(tarefas)
        elif escolha == 4:
            remover_tarefas(tarefas)
        elif escolha == 5:
            print('-'*30)
            print('Saindo do programa...')
            break
        else:
            print('\033[31mOpção inválida! Escolha de 1 a 5.\033[m')

fluxo()