# 🧠 Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## 🧾 Informações Gerais

**Aluno:** João Othávio
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
O que o programa faz:
- O programa pede ao usuário o **nome**, **idade**, e a **média**.
- Com os valores dados pelo usuário, a primeira ação que o programa faz é printar quantos anos faltam para o usuário ter 100 anos.
-Logo em seguida, ele lê a média do usuário, se ela for maior que 7, o programa printa que o usuário foi **aprovado**, seção, ele primta que o usuário foi **reprovado**.

---

### **Exercício 2 – Listas e Laços de Repetição**
O que o programa faz:
- O programa pede ao usuário **5 números inteiros** e os adiciona em uma **lista**.
- Após isso, o programa vai **calcular** todos os números adicionados a lista, fazer a média deles e guardar em uma variável chamada **media**.
- Depois, ele vai printar qual o **maior** número digitado, o **menor** número digitado, a **média** entre todos os números digitados, todos os números em forma **crescente**, e em forma **decrescente**.
- Logo depois, o programa pergunta ao usuário se ele deseja ver algum número da lista, se ele digitar algum número que **esteja** na lista, o programa mostra se o número **está** na lista e em qual **posição** ele está na **lista original**, caso contrário, o programa diz que o número **não** está na lista, e se o usuário digitar o número **-1** o programa **encerra**.

---

### **Exercício 3 – Listas Compostas e Navegação**
O que o programa faz:
- O programa começa pedindo ao usuário qual o **nome** do aluno, sua **primeira nota** e a **segunda nota**, apos isso, ele faz o cálculo da média entre as duas notas e guarda em uma variavel chamada **media**, e por fim pergunta ao usuário se deseja continuar adicionando **alunos** e **notas**.
- Depois que o usuário dizer ao programa que **não** deseja adicionar mais alunos, ele vai printar um **boletim** com a **posição** do aluno, o **nome** do aluno, e sua **média**, e logo após vai perguntar ao usuário se ele deseja ver a nota indivídual de algum aluno, se ele digitar o **índice** de algum aluno, vai aparecer seu **nome** e suas **notas**, e se ele digitar **-1** o programa encerra.

---

### **Exercício 4 – Funções e Dicionários**
O que o programa faz:
- O programa já tem uma função que faz a **média** das notas do **aluno**, se média dele for **igual** ou **maior** que **7** o aluno está **Aprovado**, e se for abaixo de **7** ele está **Reprovado**, após isso, ele retorna todos os valores em um **dicionario**.
- No funcionamento do programa, de início ele pede ao usuário o **nome** do aluno, e **duas notas** dele. O programa repete isso **três** vezes, e a cada final de repetição ele chama a função, e todos os valores que foram digitados pelo usuário, irão para a função, e na função o programa fará os cálculos e retornará tudo em um **dicionário** na lista **alunos**.
- Após isso, o programa irá printar o **nome** do aluno, sua **média** e sua **situação (Aprovado/Reprovado)**.

---

### **Exercício 5 – Projeto Final: Gerenciador de Tarefas (To-Do List)**
O que o programa faz:
- O programa de início printa no terminal um **menu**, onde o usuário pode **interagir**, e toda a interação interna do menu é feita por **funções**.
- A primeira função apenas **adiciona** uma nova **tarefa** com o **nome** que o **usuário** dar a ela.
- A segunda função vai mostrar ao usuário a **lista de tarefas**, se ela estiver **vazia**, o programa diz ao usuário que ele **não** possui nenhuma tarefa, caso ele ter, o programa vai printar no terminal a **lista de tarefas** com todas as tarefas, e as tarefas **concluídas** estaram com um **x** no seu [], se não estiver concluída o [] continuará vazio até o usuário marca-lá, ou apaga-lá.
- A terceira função pergunta ao usuário qual **tarefa** ele deseja marcar como **concluída**, o programa vai marcar a tarefa como concluída na lista com o número do **índice** da tarefa na lista, se o usuário digitar um **índice** que não existe na lista, o programa diz que essa tarefa **não** existe e volta para o menu principal.
- A quarta função pergunta ao usuŕio qual **tarefa** ele deseja apagar, o programa vai apagar a tarefa com o número do índice da **tarefa** na lista, se o usuário digitar um **índice** que não existe na lsita, o programa diz que essa tarefa **não** existe e volta para o menu principal.
- Por fim, se o usuário digitar o número 5, o programa encerra.

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

- [✅] Todos os exercícios estão funcionando corretamente  
- [✅] Cada exercício tem seu próprio commit   
- [✅] O `README.md` está preenchido com meus dados  
- [✅] O código está indentado e comentado  
- [✅] Testei todos os programas antes de enviar  

---

## 🚀 Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍
