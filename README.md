# Avaliação Final – Lógica de Programação em Python

Bem-vindo(a) à **Avaliação Final** do curso básico de **Lógica de Programação em Python**!  
O objetivo deste trabalho é aplicar os principais conceitos aprendidos ao longo do curso, organizando tudo em um repositório no GitHub.

---

## Informações Gerais

**Aluno:** _[Seu nome aqui]_    
**Data de entrega:** _[Definir data]_

---

## Instruções para realização da avaliação

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

## Objetivo da Avaliação

Avaliar a capacidade de desenvolver soluções em Python utilizando:

- Entradas e saídas de dados  
- Condicionais e laços de repetição  
- Listas simples e compostas  
- Dicionários e funções  
- Lógica aplicada em um mini projeto final

Além disso, será avaliada a **organização e uso do GitHub** — cada exercício deve ter **um commit separado**, com mensagem clara e descritiva.

---

## Estrutura do Repositório

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

>  Cada arquivo corresponde a um exercício e deve ser commitado separadamente no GitHub.

---

##  Exercícios

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

##  Critérios de Avaliação

| Critério | Peso |
|----------|------|
| Funcionamento correto dos programas | 40% |
| Clareza e legibilidade do código | 20% |
| Uso adequado das estruturas de lógica | 20% |
| Organização e histórico de commits no GitHub | 10% |
| README explicativo e funcional | 10% |

---

## Boas Práticas Recomendadas

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

## Checklist Antes da Entrega

- [ ] Todos os exercícios estão funcionando corretamente  
- [ ] Cada exercício tem seu próprio commit   
- [ ] O `README.md` está preenchido com meus dados  
- [ ] O código está indentado e comentado  
- [ ] Testei todos os programas antes de enviar  

---

## Entrega

Faça o commit de todos os exercícios até a data limite informada.

Boa sorte e bom código! 🐍
