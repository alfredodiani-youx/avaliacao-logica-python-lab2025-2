def menu():
    print('-'*30)
    print('   MENU DE TAREFAS   ')
    print('-'*30)
    print('1 – Adicionar tarefa')
    print('2 – Listar tarefas')
    print('3 – Marcar tarefa como concluída')
    print('4 – Remover tarefa')
    print('5 – Sair')
    print('-'*30)

tarefas = [
    {'titulo': 'Estudar Python', 'concluida': False},
    {'titulo': 'Enviar avaliação', 'concluida': True}
]
def adicionar():
    titulo = input('Digite o título da nova tarefa: ').strip()
    if titulo:
        tarefas.append({'titulo': titulo, 'concluida': False})
        print(f'Tarefa \'{titulo}\' adicionada.')
    else:
        print('O título não pode ser vazio.')

def listar():
    if not tarefas:
        print('Não há tarefas na lista.')
        return

    print('--- LISTA DE TAREFAS ---')
    for i, tarefa in enumerate(tarefas):
        indice = i + 1
        status = '[x]' if tarefa['concluida'] else '[ ]'
        print(f'{status} {indice} - {tarefa["titulo"]}')
    print('-'*25)

def marcar():
    listar()
    if not tarefas:
        return
    
    num_tarefa = int(input('Digite o número da tarefa para marcar como concluída: '))
    indice = num_tarefa - 1
    
    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice]
        if tarefa['concluida']:
            print(f'A tarefa \'{tarefa["titulo"]}\' já estava concluída.')
        else:
            tarefa['concluida'] = True
            print(f'Tarefa \'{tarefa["titulo"]}\' concluída!')
    else:
        print('Número de tarefa inválido.')

def remover():
    listar()
    if not tarefas:
        return

    num_tarefa = int(input('Digite o número da tarefa para remover: '))
    indice = num_tarefa - 1
    
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f'Tarefa \'{tarefa_removida["titulo"]}\' removida.')
    else:
        print('Número de tarefa inválido.')

def main():
    while True:
        menu()
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            adicionar()
        elif escolha == '2':
            listar()
        elif escolha == '3':
            marcar()
        elif escolha == '4':
            remover()
        elif escolha == '5':
            print('Saindo do sistema')
            break
        else:
            print('Opção inválida. Escolha uma das opçoẽs.')

main()