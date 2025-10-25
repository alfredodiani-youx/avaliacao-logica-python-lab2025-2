#começo do código com abertura apresentável
print('='*22)
print('DIGITE O NOME DO ALUNO')
print('='*22)
#entrada de variáveis que receberam os valores injetados pelos usuários a partir dos inputs 
nome = str(input('Digite o seu nome: ')).strip() #strip para apagar os espaços indejesados
idade = int(input('Digite sua idade: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
#adicionadas duas novas variáveis para cada nota do aluno, para maior versatilidade do exercício
media = (nota1 + nota2)/2
#validação dos dados recebidos em media com estrutura de if e else
if media >= 7:
    print('='*22)
    print(f'''Nome: {nome}
Nota média: {media}
\033[32mAPROVADO\033[m''') #"\033" ou ANSI é um padrão de código usado para adicionar cores no terminal por meio de escape sequence
#SE media for maior ou igual a sete, o aluno foi aprovado e receberá até uma mensagem com cor verde
else:
    print('='*22)
    print(f'''Nome: {nome}
Nota média: {media}
\033[31mREPROVADO\033[m''')
#SE NÃO, o aluno será reprovado e receberá uma mensagem em vermelho dizendo "REPROVADO"