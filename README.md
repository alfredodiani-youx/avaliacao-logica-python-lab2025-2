# 🧠 Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## 🧾 Informações Gerais

**Aluno:** Luis Fernando    
**Data de entrega:** 27/10/2025

---

## 🧾 Instruções para realização da avaliação

Clone esse repositório no seu computador

```
git clone git@github.com:alfredodiani-youx/avaliacao-logica-python-lab2025-2.git
```

Crie uma nova branch utilizando seu nome e sobrenome 

com todas as letras em minúsculo e sem espaços ou acentos por exemplo: joao-silva

```
git checkout -b <seu_nome>
```

Lembre-se de adicionar os arquivos modificados e fazer commit após cada exercício feito

```
git add .
```

```
git commit -m <sua_mensagem>
```

Envie as modificações para o repositório assim que possível:

```
git push origin
```

Antes de entregar o exercício **reescreva** esse README explicando com suas palavras o que cada exercício faz incluindo as funcionalidades princiais e as adicionadas por você.

Certifique-se de cumprir os requisitos de cada exercício.

Caso queira adicionar alguma funcionalidade extra sinta-se à vontade.

---

## 🎯 Objetivo da Avaliação

Avaliar a capacidade de desenvolver soluções em Python utilizando:

- Entradas e saídas de dados  
- Condicionais e laços de repetição  
- Listas simples e compostas  
- Dicionários e funções  
- Lógica aplicada em um mini projeto final

Além disso, será avaliada a **organização e uso do GitHub** — cada exercício deve ter **um commit separado**, com mensagem clara e descritiva.

---

## ⚙️ Estrutura do Repositório

Seu repositório deve seguir esta estrutura:

```
avaliacao-logica-python-seu-nome/
│
├── exercicio1.py
├── exercicio2.py
├── exercicio3.py
├── exercicio4.py
├── exercicio5_todolist.py
└── README.md
```

> 💡 Cada arquivo corresponde a um exercício e deve ser commitado separadamente no GitHub.

---

## 🧩 Exercícios

### **Exercício 1 – Entrada, Processamento e Saída**
Explicação: 
Eu crio três variáveis chamadas nome, idade e nota média, cada uma delas eu peço uma informação para o usuário.
Crio uma variável chamada idadeMais100Anos para receber a operação que calcula a idade da pessoa daqui 100 anos.
faço um print para separar as perguntas com o resultado.
faço outro print para imprimir todas as informações digitas e quantos anos resta para a pessoa chegar a 100 anos.
E faço um if e else para calcular se a pessoa está aprovada ou reprovada, com a média que vale 7

---

### **Exercício 2 – Listas e Laços de Repetição**
Explicação: 
crio uma lista chamada numerosInteiros e depois mais duas variáveis (maiorInteiro, menorInteiro) que recebe o valor 0.
faço um laço de tamanho 5 que irá pedir 5 números inteiros, depois calculo a média de todos os valores.
pego a varável menorInteiro e faço um min(numerosInteiros) para achar o menor número digitado dentro da lista numerosIntreiros.
e com a variável maiorInteiro faço um max(numerosInteiros) para achar o maior número digitado dentro da lista númerosInteiros.
faço um print para separar o resultado e fazer um cabeçalho para os resultados.
1º print para imprimir o maior número da lista.
2º print para imprimir o menor número da lista
3º print para imprimir a média dos 5 números digitados
4º print para imprimir a lista em ordem crescente, usando sorted.
pego a lista numerosInteiros e faço um .sort(reverse=True) para inverter a lista.
5º print para imprimir a lista em ordem decrescente.

crio uma variável para a posição de cada número e nela peço para o usuário digitar um número.
uso if e else para verificar se o número que o usuário digitou está ou não dentro da lista.
Se ele estiver cria uma variável chamada posicao que recebe o valor indice do número digitado pelo usuário, e logo em  seguida faço um print para dizer o usuário que o número está na lista e dizer também em qual posicao da lista ele está.
Se ele não estiver faço um print para informar ao usuário que o número que ele digitou, não está na lista. 

---

### **Exercício 3 – Listas Compostas e Navegação**
explicação:
A lista alunos armazena todos os dados de cada aluno.
lista de notas armazena as notas temporariamente as notas de cada aluno.
lista de nomes guarda sublistas de cada aluno.
continuar = 'S': controla se o usuário quer continuar adicionando alunos.

No cadastro de alunso e notas pede o nome do aluno e adiciona na lista alunos.
dentro de um loop interno, pede as nota do aluno, adicionando cada nota na lista de notas.
após finalizar as notas do aluno, adiciona nome e notas na lista de nomes.
pergunta se o usuário quer cadastrar outro aluno se ele quiser entra no loop novamente.

Mostrar o boletim:
exibe um cabeçalho com Nº, ALUNO e MÉDIA.
percorre na lista de nomes e calcula a média das notas.
mostra o índice, o nome do aluno e a média.

Consultar notas detalhadas:
Permite que o usuário digite o índice de um aluno e consultar todas as notas dele.
pega os dados da sublista nome e notas na lista de nomes.
imprime o nome do aluno, suas notas e a média.
e no final pergunta se o usuário quer consultar outro aluno. Se ele não quiser o programa finaliza

---

### **Exercício 4 – Funções e Dicionários**
explicação:
Crio uma função chamada analisar_aluno que recebe os parâmetros nome e notas.
dentro dessa função, analisa se a média do aluno está boa ou ruim, se estiver acima ou igual a 7 cria uma variável chamada situacao que recebe 'Aprovado', se ele estiver abaixo de 7 a mesma variável situacao começa a receber 'Reprovado'.
e retorna um dicionário que tem os indices nome, media e situacao.

NO PROGRAMA PRINCIPAL:
crio uma lista chamada alunos que guarda os dados do dicionário.
crio um laço de tamanho 3.
que recebe uma variável nome 
faço um print para separar o restante das informações.
crio uma lista de notas e uma variável 'continuarNotas' que recebe 'S' que é a minha cindição de parada.
crio um loop que enquanto a condição de parada for igual 'S', pede uma nota.
na lista notas eu du append na variavel que recebeu a nota "notas.append(nota)"
agora a varial "continuarNotas" começa a receber uma pergunta, que pergunta se eo usuário deseja adicionar outra nota ou não, se ele digitar 'S' ele entra no loop novamente, Já se ele digitar 'N' sai do loop e retorna pro laço for.
faço a lista alunos .append a função analisar_notas com os parametros nome e notas.
faço um print para pular linha.
um para o cabeçalho e o outro para separar as informações.
faço outro laço que para cada estudante dentro da lista alunos faz 4 prints.
1º imprime o nome de cada estudante de acordo com a ordem digitada.
2º imprime a média de cada aluno com 1 casa decimal.
3º imprime a situação de cada aluno: Aprovado ou Reprovado.
4º imprime uma linha de tamanho 40.

---

### **Exercício 5 – Projeto Final: Gerenciador de Tarefas (To-Do List)**
quando abre o programa aparece um menu com 5 opções: adicionar tarefa, listar tarefas, marcar tarefa como concluída remover tarefas e sair.

para cada opção tem uma função.
função MENU:
imprime um menu com opções para o usuário.


função ADICIONAR TAREFA:
recebe o parâmetro tarefas,
digita o nome da tarefa e ela registra na lista tarefas.
uso um if e else para verificar se existe uma tarefa e se existir a lista recebe um dicionário que nele tem os índices: titulo, e concluida, o indice tarefa recebe o nome da tarefa e o indice concluida recebe False porque a tarefa ainda não foi concluída.
se não for digitado nada no nome da tarefa imprime uma mensagem em vermelho dizendo que o nome da tarefa é inválido.

função LISTA DE TAREFAS:
recebe o parâmetro tarefas, 
imprime um cabeçalho de LISTAGEM DE TAREFAS.
if não tiver nenhuma tarefa na lista tarefas, imprime uma mensagem em vermelho dizendo que nenhuma tarefa foi cadastrada
se foi cadastrada alguma tarefa,
cria um laço que recebe indice que começa em 1 e cada tarefa qu esteja dentro da lista tarefas enumerando a lista tarefas por indices.
cria uma variável status que recebe "[x]" if a tarefa foi concluída e se não foi, recebe um colchete vazio.
imprime formatado o status ([x] ou [ ]) o indice e o nome da tarefa.
imprime uma linha de tamanho 30 para separar as informações.

função MARCAR CONCLUÍDA:
recebe o parâmetro tarefas,
chama a lista de tarefas com o parâmetro tarefas,
e se não tiver tarefa dentro da lista tarefas
retorna ao menu.
se terminar uma tarefa pode informar o número correspondente a tarefa, e o programa marca ela como feita. se ela já estiver concluída ele avisa com uma mensagem vermelha.

função REMOVER TAREFAS:
recebe o parametro tarefas,
chama a lista de tarefas com o parametro tarefas.
Quando uma tarefa não é mais necessária você pode apagar ela da lista informando o número correspondente. O programa confirma qual tarefa foi concluída.

função FLUXO:
controla todo o funcionamento do programa.
inicializa ua lista para guardar todas as tarefas que o usuário cadastrar.
Mostra o menu com as opções disponiveis.
entra em um loop infinito que só sai se o usuário escolher a opção de sair.
Dependendo da opção escolhida pelo usuário:
opção 1:
chama a função ADICIONAR TAREFAS
opção 2:
chama a função LISTA DE TAREFAS
opção 3:
chama a função MARCAR COMO CONCLUIDA
opção 4:
chama a função REMOVER TAREFAS
opção 5:
imprime uma mensgaem de saida em vermelho e encerra o loop finalizando o programa.

se o usuário digitar um número que não está estre 1 e 5, o programa avisa que a opcção é inválida.




---

## 🧮 Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Funcionamento correto dos programas | 40% |
| Clareza e legibilidade do código | 20% |
| Uso adequado das estruturas de lógica | 20% |
| Organização e histórico de commits no GitHub | 10% |
| README explicativo e funcional | 10% |

---

## 💡 Boas Práticas Recomendadas

- Use **nomes claros** para variáveis e funções.  
- Faça **comentários curtos** explicando trechos importantes.  
- Evite código duplicado.  
- Teste seus programas antes de subir para o GitHub.  
- Faça commits **com mensagens descritivas**, por exemplo:
  ```
  feat: exercício 3 – cadastro e boletim de alunos
  fix: corrigido cálculo de média
  ```

---

## ✅ Checklist Antes da Entrega

- [x] Todos os exercícios estão funcionando corretamente  
- [x] Cada exercício tem seu próprio commit   
- [x] O `README.md` está preenchido com meus dados  
- [x] O código está indentado e comentado  
- [x] Testei todos os programas antes de enviar  

---

## 🚀 Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍
