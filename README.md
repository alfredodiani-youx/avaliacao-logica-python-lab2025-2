# 🧠 Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## 🧾 Informações Gerais

**Aluno:** _[Isabela Milene Soares Clemente]_    
**Data de entrega:** _[27/10/2025]_

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
├── exercicio2.py
├── exercicio4.py
├── exercicio5_todolist.py
└── README.md
```

> 💡 Cada arquivo corresponde a um exercício e deve ser commitado separadamente no GitHub.

---

## 🧩 Exercícios

### **Exercício 1 – Entrada, Processamento e Saída**
Crie um programa que:
- Peça ao usuário **nome**, **idade** e **nota média** (float).
- Calcule:
  - Daqui quantos anos o usuário terá 100 anos.
  - Se a nota média é **acima da média da turma (>= 7.0)** ou não.
- Exiba uma mensagem formatada com todas as informações.

---

### **Exercício 2 – Listas e Laços de Repetição**
Crie um programa que:
- Leia **5 números inteiros** e armazene-os em uma lista.
- Exiba:
  - O **maior**, **menor** e **média** dos valores.
  - A lista em **ordem crescente e decrescente**.
- Peça um número e informe se ele está na lista e em qual posição.

---

### **Exercício 3 – Listas Compostas e Navegação**
Crie um programa que registre **nome** e **notas** de **vários** alunos.
- Estruture os dados como:
  ```python
  alunos = [[nome, [nota1, nota2]], ...]
  ```
- Mostre um boletim com nome e média.
- Permita consultar as notas de um aluno pelo número de índice.

---

### **Exercício 4 – Funções e Dicionários**
Crie uma função `analisar_aluno(nome, notas)` que:
- Recebe o nome e uma lista de notas.
- Retorna um dicionário:
  ```python
  {"nome": "Maria", "media": 8.5, "situacao": "Aprovado"}
  ```
- No programa principal, cadastre 3 alunos e exiba o relatório completo.

---

### **Exercício 5 – Projeto Final: Gerenciador de Tarefas (To-Do List)**
Crie um **sistema simples de tarefas** separando as funcionalidades em funções no Python.
O sistema deve ter um menu interativo:

```
1 – Adicionar tarefa
2 – Listar tarefas
3 – Marcar tarefa como concluída
4 – Remover tarefa
5 – Sair
```

As tarefas devem ser armazenadas como **lista de dicionários**:
```python
tarefas = [
    {"titulo": "Estudar Python", "concluida": False},
    {"titulo": "Enviar avaliação", "concluida": True}
]
```

Ao listar tarefas:
```
[ ] 1 - Estudar Python
[x] 2 - Enviar avaliação
```

O programa só termina quando o usuário escolher “Sair”.

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

- [ ] Todos os exercícios estão funcionando corretamente  
- [ ] Cada exercício tem seu próprio commit   
- [ ] O `README.md` está preenchido com meus dados  
- [ ] O código está indentado e comentado  
- [ ] Testei todos os programas antes de enviar  

---

## 🚀 Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍

## Explicando oque cada um do meus programas faz!

EXERCÍCIO 01
Mostra uma mensagem dizendo “Nome, Idade, nota, quantos anos daqui 100 anos”.
Pede pra pessoa digitar o nome, a idade e a nota média.
Calcula quantos anos faltam pra pessoa fazer 100 anos.
Checa se a nota é 7 ou mais e fala se tá acima ou abaixo da média da turma.
Mostra tudo na tela: nome, idade, nota e se tá acima ou abaixo da média.
Diz quantos anos faltam pra chegar a 100 ou avisa se a pessoa já tem 100 anos ou mais.
Basicamente, ele pega os dados que você digita, faz umas continhas e mostra um resumão na tela.


 EXERCÍCIO 02 
Mostra a mensagem “Digite 5 números inteiros:”.
Pede pra pessoa digitar 5 números, um por vez, e guarda todos numa lista.
Mostra a lista completa com todos os números digitados.
Descobre qual é o maior número, qual é o menor e a média desses números.
Mostra na tela o maior número, o menor e a média.
Cria uma versão da lista em ordem crescente e outra em ordem decrescente e mostra na tela.
Pede pra pessoa digitar um número e verifica se ele está na lista.
Se o número estiver, mostra em qual posição da lista ele está.
Se não estiver, avisa que o número não está na lista.
   

EXERCÍCIO 03
Cria uma lista vazia chamada alunos.
Entra num loop pedindo para cadastrar alunos
Pede o nome do aluno.
Pede a nota 1 e nota 2.
Coloca tudo na lista alunos como [nome, [nota1, nota2]].
Pergunta se quer cadastrar outro aluno. Se a pessoa digitar “n”, para de pedir.
Mostra na tela um boletim com todos os alunos
Cada aluno aparece com o número dele, nome e média das notas.
Entra em outro loop perguntando qual aluno a pessoa quer ver as notas detalhadas
Se digitar um número válido, mostra as duas notas do aluno.
Se digitar 999, sai do loop.
Se digitar um número que não existe, avisa que é inválido.
Basicamente, o programa cadastra vários alunos, mostra a média de cada um e permite ver as notas detalhadas de qualquer aluno.



EXERCÍCIO 04
Eu criei uma função chamada analisar_aluno que recebe o nome e as duas notas de um aluno.
Calcula a média das notas.
Fala se o aluno está Aprovado (média >= 7) ou Reprovado.
Me devolve essas coisas que pedi em um dicionário com nome, média e situação.
Depois eu crio uma lista chamada alunos pra guardar todos os dicionários.
Eu peço pra cadastrar 3 alunos
Pergunto o nome, a nota 1 e a nota 2.
Uso a função analisar_aluno pra criar o dicionário e coloco na lista alunos.
No final, eu mostro na tela um relatório com todos os alunos e as informações que a função deu.
Resumindo, meu programa pega nome e notas de 3 alunos, calcula a média, fala se passou ou não e mostra tudo organizado no final.



EXERCÍCIO 05
Eu começo com uma lista vazia chamada tarefas.
Eu criei algumas funções pra organizar tudo
adicionar_tarefa() pede o título da tarefa e coloca na lista como não concluída.
listar_tarefas() mostra todas as tarefas com um “[ ]” se não tá feita e “[x]” se tá concluída.
marcar_concluida() deixa eu escolher uma tarefa e marcar como feita.
remover_tarefa() deixa eu escolher uma tarefa e apagar da lista.
Depois eu faço um menu que fica rodando até eu escolher sair
Opção 1 adiciona tarefa.
Opção 2 mostra a lista.
Opção 3 marca uma tarefa como concluída.
Opção 4 remove uma tarefa.
Opção 5 sai do programa.
Qualquer outra coisa dá aviso de “Opção inválida”.
Resumindo, meu programa me deixa gerenciar minhas tarefas adicionar, ver, marcar como feita e remover, tudo pelo menu.
