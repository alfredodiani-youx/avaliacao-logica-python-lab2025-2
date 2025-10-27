to_do_list=[] #váriavel que cria uma to do list vazia
dict= {} #váriavel que cria um dicionário vazio
def adicionar (atividade): #função que recebe um parâmetro (atividade= nome da tarefa) e tem como objetivo adicionar novas tarefas para a to do list
    dict = {'TAREFA': atividade, 'CONCLUSÃO': False} #variável que cria o modelo de atribuição do dict, atribuindo o nome da tarefa e a conclusão como false até ser marcada como concluída
    to_do_list.append(dict)#método que adiciona o dicionário na to do list
def listar(): #função que tem como objetivo listar a to-do list
    listagem= f'As tarefas são {to_do_list}' #váriavel que tem como valor a string formatada com todas as tarefas
    return listagem #return que retorna a váriavel listagem
def remover(r): #função que recebe um parâmetro(r=nome da tarefa que o usuário deseja ser removida) e tem como objetivo remover uma tarefa da to-do list
    for item in to_do_list: #laço for que verifica cada dicionário dentro da to-do list
        if item['TAREFA']== r: #condição que verifica qual dicionário tem o valor da key ['TAREFA'] igual ao nome da tarefa que o usuário deseja remover
            to_do_list.remove(item) #método que remove o dicionário que tem a tarefa que o usuário deseja remover
def concluida(c): #função que recebe um parâmetro(c=nome da tarefa que o usuário deseja marcar como concluída) e tem como objetivo marcar a tarefa como concluida (substituir o valor false da key ['CONCLUSÃO'] para True)
    for item in to_do_list: #laço for que verifica cada dicionário na to-do list
        if item['TAREFA']== c: #condição que verifica se a key tarefa de algum dicionário tem como valor o nome da tarefa concluida
            item['CONCLUSÃO'] = True #substituição do valor false pelo true
menu= 1000 #váriavel com valor 1000 para que o while a seguir rode
while menu != 5: #laço while que terá interrupção quando a váriavel menu possuir valor igual à 5
    menu=int(input("""Qual função de nosso menu você quer selecionar? 
          [1] Adicionar tarefa
          [2] Listar tarefa
          [3] Marcar como conclúida
          [4] Remover tarefa
          [5] Sair do programa """)) #váriavel que imprime o menu e suas funcionalidades e pergunta ao usuário qual funcionalidade ele quer selecionar
    if menu == 1: 
        adicionar(atividade= str(input('Digite a tarefa que você deseja anotar: ')).upper()) #condição que caso a opção selecionado no menu seja adicionar, será feito o chamado da função adicionar
    if menu == 2: #condição que caso a opção selecionado no menu seja adicionar, será feito o chamado da função listar
        print(listar())
    if menu == 3:#condição que caso a opção selecionado no menu seja adicionar, será feito o chamado da função concluida
        concluido= str(input('Qual tarefa você concluiu?').upper())
        concluida(concluido)
    if menu == 4: #condição que caso a opção selecionado no menu seja adicionar, será feito o chamado da função remover
        remocao= str(input('Digite o nome da tarefa que você deseja remover: '))
        remover(remocao)