def analisarAluno(n, d, e): #função que recebe três parâmetros (n=nome, d= nota1, e=nota2)
    aluno={}#váriavel que cria um dicionário vazio
    media= (d+e)/2#variável que soma a nota 1 e 2 e as divide por 2, tendo como resultado uma média
    if media >= 5.0: #condição que define que se a media for maior ou igual a 5 a situação do aluno será de aprovação, caso contrário, a situação será de reprovação
        situacao= 'Aprovado'
    else:
        situacao='Reprovado'
    aluno['NOME']= n #váriavel que cria a key ['NOME'] no dicionário aluno e atribui como valor da key o nome
    aluno['MEDIA']= media #váriavel que cria a key ['MEDIA'] no dicionário aluno e atribui como valor da key a média
    aluno['SITUAÇÃO']= situacao #váriavel que cria a key ['SITUAÇÃO'] no dicionário aluno e atribui como valor da key a situação do aluno
    return aluno #return que retorna o dicionário


for c in range (1, 4): #laço for que se repete 3 vezes perguntando os dados do aluno e criando o dicionário para ele
    nome=str(input('Digite o nome do aluno: '))
    nota1= float(input('Digite a nota 1 do aluno: '))
    nota2= float(input('Digite a nota do 2 aluno: '))
    print(f'A análise do aluno é: {analisarAluno(nome, nota1, nota2)} ')