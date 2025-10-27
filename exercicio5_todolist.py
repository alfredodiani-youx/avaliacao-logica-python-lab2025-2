tarefas = []

def adicionar_tarefa(titulo):
    tarefa = {
        "titulo": titulo,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f'\033[32mNova tarefa "\033[34m{titulo}\033[32m" adicionada\033[m')

def listar_tarefas():
    print('\033[35m=== LISTA DE TAREFAS ===\033[m')
    if not tarefas:
        print('\033[33mNenhuma tarefa cadastrada.\033[m')
        return
    
    for i, tarefa in enumerate(tarefas, 1):
        status = '[x]' if tarefa['concluida'] else '[ ]'
        cor = '\033[32m' if tarefa['concluida'] else '\033[33m'
        print(f'{cor}{status} {i} - {tarefa["titulo"]}\033[m')


def marcar_concluida(indice):
    if 0 < indice <= len(tarefas):
        tarefa = tarefas[indice-1]
        tarefa['concluida'] = True
        print(f'\033[32mTarefa "{tarefa["titulo"]}" marcada como concluída!\033[m')
    else:
        print('\033[31mÍndice de tarefa inválido!\033[m')


def remover_tarefa(indice):
    if 0 < indice <= len(tarefas):
        tarefa = tarefas.pop(indice-1)
        print(f'\033[32mTarefa "{tarefa["titulo"]}" removida com sucesso!\033[m')
    else:
        print('\033[31mÍndice de tarefa inválido!\033[m')

def menu():
    print('\033[35m=== MENU PRINCIPAL ===\033[m')
    opcoes = [
        'Ver Tarefas',
        'Nova Tarefa',
        'Marcar Como Concluída',
        'Remover Tarefa',
        'Sair'
    ]
    
    for i, opcao in enumerate(opcoes, 1):
        print(f'\033[32m{i}\033[m - {opcao}')
    print()
    
    while True:
        try:
            escolha = int(input('\033[33mSua opção: \033[32m'))
            if 1 <= escolha <= len(opcoes):
                return escolha
            print('\033[31mOpção inválida! Digite um número entre 1 e 5.\033[m')
        except ValueError:
            print('\033[31mPor favor, digite um número!\033[m')

def main():
    print('\033[35m=== SISTEMA DE TAREFAS v1.0 ===\033[m')
    print()

    while True:
        resposta = menu()
        if resposta == 1:  # Ver Tarefas
            listar_tarefas()
        elif resposta == 2:  # Nova Tarefa
            print('\033[35m=== NOVA TAREFA ===\033[m')
            titulo = input('\033[33mDescrição da tarefa: \033[32m').strip()
            if titulo:
                adicionar_tarefa(titulo)
            else:
                print('\033[31mA descrição não pode estar vazia!\033[m')
        elif resposta == 3:  # Marcar Como Concluída
            print('\033[35m=== MARCAR COMO CONCLUÍDA ===\033[m')
            listar_tarefas()
            try:
                indice = int(input('\033[33mNúmero da tarefa a concluir: \033[32m'))
                marcar_concluida(indice)
            except ValueError:
                print('\033[31mPor favor, digite um número válido!\033[m')
        elif resposta == 4:  # Remover Tarefa
            print('\033[35m=== REMOVER TAREFA ===\033[m')
            listar_tarefas()
            try:
                indice = int(input('\033[33mNúmero da tarefa a remover: \033[32m'))
                if 0 < indice <= len(tarefas):
                    confirmacao = input(f'Confirma a remoção da tarefa "{tarefas[indice-1]["titulo"]}"? [S/N] ').strip().upper()
                    if confirmacao == 'S':
                        remover_tarefa(indice)
                else:
                    print('\033[31mÍndice de tarefa inválido!\033[m')
            except ValueError:
                print('\033[31mPor favor, digite um número válido!\033[m')
        elif resposta == 5:  # Sair
            print('\033[32m=== Sistema Finalizado. Até logo! ===\033[m')
            break
        print()  # Linha em branco para melhor visualização 

if __name__ == '__main__':
    main()
    