# 🧠 Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## 🧾 Informações Gerais

**Aluno:** _Daniella_    
**Data de entrega:** _27/10/25_

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
O código pede ao usuário seu **nome**(str), **idade**(int) e **média**(float). Depois, calcula quantos anos faltam para ele completar 100 anos.
Em seguida, verifica(if e else) se o usuário está acima ou abaixo da média (supondo que seja 7, como exemplificado) e mostra para o usuário.
Por fim, exibe(print) um resumo com todas as informações digitadas e o resultado do cálculo.

### **Exercício 2 – Listas e Laços de Repetição**
Esse código começa pedindo(input) que o usuário digite cinco valores, que são guardados em uma lista chamada **valores**.
Depois que todos os valores são digitados, o programa faz alguns cálculos e amostraçoẽs: mostra a lista completa, o **maior** e o **menor** número, e também calcula a **média** dos valores.
Depois, o código organiza a lista em **ordem crescente** e **decrescente**, mostrando essas duas versões na tela.

Por último, o programa pede que o usuário digite um número para **procurar** na lista.
Se(if e else) o número estiver na lista, ele informa **em qual posição** da lista o número aparece; caso contrário, mostra uma mensagem dizendo que o número **não foi encontrado**.

### **Exercício 3 – Listas Compostas e Navegação**
O programa serve para **registrar alunos e as suas notas**. Ele começa pedindo o nome de um aluno e permite que o usuário cadastre **quantas notas quiser**(while) para esse aluno. Cada aluno é armazenado em uma lista, junto com suas notas.
Depois de cadastrar um aluno, o programa pergunta se o usuário quer cadastrar outro. Esse processo continua até o usuário responder **“N”**.
Em seguida, o programa **mostra uma lista de todos os alunos**, numerando cada um. Para que assim, cada aluno fica com um número para facilitar a busca.
Assim, o usuário pode digitar o número de um aluno para **ver suas notas**. 
**Esse processo de pesquisa continua até o usuário digitar **“fim”**, encerrando o programa.**


### **Exercício 4 – Funções e Dicionários**
O programa serve para **olhar sua situação** de acordo suas notas.
Primeiro, ele define uma **função**(def) que calcula a **média das notas** e determina a **situação** do aluno. Essa função compara a média com as condiçoẽs definidas: se a média for **7 ou maior**, o aluno está **aprovado**; se ficar entre **5 e 6,9**, está em **recuperação**; e se for **menor que 5**, está **reprovado**.
Depois, o programa pede ao usuário que **digite o nome e as notas de três alunos**. Para cada aluno, ele guarda as informações e chama a função para fazer o cálculo da média e descobrir a situação. O resultado de cada aluno (nome, média e situação) é guardado em uma lista de dicionários, que ajuda na organização dos dados.
No final, o programa mostra um **resumo com todos os alunos**, mostando o nome de cada um, sua média e se foi aprovado, ficou em recuperação ou foi reprovado.


### **Exercício 5 – Projeto Final: Gerenciador de Tarefas (To-Do List)**
O programa é um **gerenciador de tarefas simples**, que permite ao usuário organizar suas tarefas. Ele mostra quatro opçoẽs: **adicionar tarefas, listar tarefas, marcar tarefas como concluídas e remover tarefas**.
Cada tarefa é armazenada em uma lista como um **dicionário**, contendo o nome da tarefa e um indicador se ela foi concluída ou não. Quando o usuário escolhe adicionar uma tarefa, o programa pede o nome e cria esses dados com o status inicial como “não concluída”.
Ao listar tarefas, o programa mostra todas as tarefas cadastradas, numeradas, e indica com símbolos se cada uma está concluída ou pendente. Para marcar uma tarefa como concluída ou tira-la, o usuário digita o número correspondente à tarefa, e o programa remove a tarefa da lista.
O programa funciona dentro de um **loop**, exibindo um menu de opções até que o usuário escolha sair.

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
- [x] Cada exercício tem seu próprio commit   
- [x] O `README.md` está preenchido com meus dados  
- [x] O código está indentado e comentado  
- [x] Testei todos os programas antes de enviar  

---

## 🚀 Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍
