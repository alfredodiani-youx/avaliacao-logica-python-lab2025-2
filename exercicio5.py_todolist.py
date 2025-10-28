#declarando uma variável lista global e também as funções de cada funcionalidade

def menu():
    tarefas = []
    #while para deinir 
    while True:
        print('='*30)
        print('Lista de Tarefas')
        print('='*30)
        print('''
              1 - Adicionar tarefas
              2 - Listar tarefas
              3 - Marcar tarefas como concluída
              4 - Remover tarefas
              5 - Sair\n''')
        opc = int(input('Digite a opção desejada: '))
        if opc == 1:
            adicionarTarefa(tarefas)
        elif opc == 2:
            listarTarefas(tarefas)
        elif opc == 3:
            marcarTarefa(tarefas)
        elif opc == 4:
            removerTarefa(tarefas)
        elif opc == 5:
            print('<SAINDO>')
            break 

def adicionarTarefa(tarefas):
    título = str(input('Digite o título da tarefas: ')).strip()
    tarefas.append({'Título': título, 'Concluída': False})
    print('<TAREFA ADICIONADA COM SUCESSO>')
def listarTarefas(tarefas):
    print()
    print('='*30)
    print('Tarefas')
    print('='*30)
    for c, tarefa in enumerate(tarefas, start=1):
        if tarefa['Concluída']:
            print(f'[ x ] {c} ->', tarefa['Título'])
        else:
            print(f'[   ] {c} ->', tarefa['Título'])

def marcarTarefa(tarefas):
    listarTarefas(tarefas)
    try:
        print('=' * 30)
        marcador = int(input('Digite o índice da tarefa que você deseja modificar: ')) - 1
        if tarefas[marcador]['Concluída']:
            print('<TAREFA JÁ CONCLUÍDA>')
        elif not tarefas[marcador]['Concluída']:
            tarefas[marcador]['Concluída'] = True
    except:
        print('<TAREFA NÃO ENCONTRADA>')
    
def removerTarefa(tarefas):
    listarTarefas(tarefas)
    print('=' * 30)
    try:
        marcador = int(input('Digite o índice da tarefa que você deseja remover: ')) - 1
        if tarefas[marcador]:
            del(tarefas[marcador])
    except:
        print('<TAREFA NÃO ENCONTRADA>')
def main():
    while True:
        menu()
        break
if __name__ == "__main__":
    main()