# 🧠 Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## 🧾 Informações Gerais

**Aluno:** Agatha    
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
O programa pede que o usuário digite seu nome, idade e nota média.
Em seguida, ele calcula quantos anos faltam para o usuário completar 100 anos e verifica se a nota está acima ou abaixo da média da turma (considerando o 7 como média).
Depois, o programa exibe mensagens personalizadas, mostrando o nome, a idade, quanto falta para 100 anos e a situação da nota.
---

### **Exercício 2 – Listas e Laços de Repetição**
Explicação:
O programa pede que o usuário digite 5 números, que são armazenados em uma lista.
Em seguida, ele calcula a média dos valores, mostra o maior e o menor número, e exibe a lista em ordem crescente e decrescente.
Depois, o usuário digita um número para o programa verificar se ele está presente na lista.
Se estiver, o programa mostra a posição em que o número aparece, se não estiver, informa que ele não foi encontrado.
---


### **Exercício 3 – Listas Compostas e Navegação**
Explicação:
O programa serve para cadastrar alunos, guardar suas notas e permitir consultas depois.
Ele usa listas para armazenar os dados e laços while para repetir as ações até o usuário decidir parar.
Primeiro, o programa pede o nome do aluno e permite que o usuário digite quantas notas quiser.
Depois de registrar cada aluno com suas notas, ele guarda tudo em uma lista principal chamada listadealunos.
Em seguida, o programa calcula a média das notas de cada aluno e mostra uma lista geral com os nomes e médias.
Por fim, o usuário pode consultar as notas completas de um aluno específico digitando o número de índice correspondente.
---

### **Exercício 4 – Funções e Dicionários**
Explicação:
O programa pega uma lista de alunos e notas que já estão prontas no código e faz uma análise de cada um.
Ele usa uma função que calcula a média das notas e define se o aluno está aprovado ou reprovado.
Depois, ele percorre a lista, aplica a função em cada aluno e guarda os resultados em outra lista de relatórios.
No final, o programa mostra um resumo bem organizado de cada aluno, com nome, média e situação.
---

### **Exercício 5 – Projeto Final: Gerenciador de Tarefas (To-Do List)**
Explicação:
O programa vai funcionar como um assistente simples para sua lista de tarefas.
Eu organizei o código em pequenas partes (funções) para cada ação:
Uma função mostra o menu com as opções (Adicionar, Listar, etc.).A função principal fica repetindo o menu e aguardando sua escolha.
Quando você escolhe uma opção (como adicionar), a função correspondente entra em ação e modifica a lista global de tarefas.
A lista de tarefas se atualiza conforme você insere ou remove itens. Ele só encerra quando você escolhe a opção "Sair"---
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

- [X] Todos os exercícios estão funcionando corretamente  
- [X] Cada exercício tem seu próprio commit   
- [X] O `README.md` está preenchido com meus dados  
- [X] O código está indentado e comentado  
- [X] Testei todos os programas antes de enviar  

---

## 🚀 Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍
