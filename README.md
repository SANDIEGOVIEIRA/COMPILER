# 🧠 Projeto de Compiladores - Análise Léxica, Sintática e Semântica

Este projeto implementa um compilador simples em Python, usando a biblioteca **PLY (Python Lex-Yacc)**, capaz de realizar:

- ✅ Análise Léxica
- ✅ Análise Sintática
- ✅ Análise Semântica
- ✅ Construção de AST
- ✅ Detecção de tokens inválidos
- ✅ Suporte a estruturas `if`, `while`, `for` e funções

---

## ⚙️ Requisitos

- Python 3.10 ou superior
- PLY (Python Lex-Yacc)

### 💻 Instalação do PLY:

```bash
pip install ply
````

---

## ▶️ Como Executar o Compilador

O compilador principal é executado pelo arquivo `main.py`, que recebe um arquivo `.src` como entrada.

```bash
python main.py testes/nome_do_arquivo.src
```

---

## 🗂 Estrutura do Projeto

```
compiler/
├── main.py               # Arquivo principal do compilador
├── lexer.py              # Analisador léxico (tokens)
├── parser.py             # Analisador sintático (gramática + AST)
├── semantic.py           # Analisador semântico (verificação de tipos, escopo)
├── ast_nodes.py          # Definição dos nós da AST
├── parsetab.py           # Gerado automaticamente pela PLY
├── testes/
│   ├── teste_lex.src
│   ├── teste_bool.src
│   ├── teste_func.src
│   ├── teste_not.src
│   ├── teste_ast.src
│   ├── teste_for.src
│   ├── teste_semantica.src
│   ├── teste_erro_semantica.src
│   └── teste_full.src
```

---

## 🧪 Comandos de Teste por Funcionalidade

### 1. 🔍 **Teste Léxico – Tokens Inválidos**

```bash
python -c "import lexer; data=open('testes/teste_lex.src').read(); lexer.lexer.input(data); [tok for tok in lexer.lexer]; print(lexer.lexer.invalid_tokens)"
```

📄 Entrada: `teste_lex.src`
🎯 Verifica reconhecimento de tokens inválidos como `@`, `$`

---

### 2. 🔄 **Fluxo de Tokens**

```bash
python lexer.py
```

🎯 Gera sequência de tokens válidos a partir de um trecho de código embutido

---

### 3. 🌳 **Análise Sintática com AST**

```bash
python main.py testes/teste_ast.src
```

🎯 Gera árvore sintática com `for` e atribuições encadeadas

---

### 4. 🧠 **Análise Semântica – Condicional e Laço**

```bash
python main.py testes/teste_semantica.src
```

🎯 Verifica uso correto de tipos e escopo com `if`, `else` e `while`

---

### 5. ❌ **Erro Semântico – Variável sem Tipo**

```bash
python main.py testes/teste_erro_semantica.src
```

🎯 Detecta erro ao usar uma variável (`sum`) antes de definição de tipo

---

### 6. 🧪 **Booleanos e Operadores Lógicos**

```bash
python main.py testes/teste_bool.src
```

🎯 Usa `true`, `false`, `!`, `||` em condição `if`

---

### 7. ❕ **Negação com `!` e `&&`**

```bash
python main.py testes/teste_not.src
```

🎯 Testa combinação de operadores lógicos com negados

---

### 8. 📦 **Declaração de Função**

```bash
python main.py testes/teste_func.src
```

🎯 Verifica função `add(a, b)` com retorno

---

### 9. 🔁 **Laço `for` com Acumulação**

```bash
python main.py testes/teste_for.src
```

🎯 Loop de 1 a 5 somando valores em `sum`

---
### 🔚 Teste Completo – for, função e if

```bash
python main.py testes/teste_full.src
```

🎯 Executa múltiplas estruturas de forma encadeada
⚠️ Inclui propositalmente um token inválido % para testar erros

---
### 🧪 Executar todos os testes de uma vez:

```bash
python run_all_tests.py
```
Isso executará todos os testes `.src` na pasta `/testes`, incluindo análise léxica, sintática e semântica.

---
## Todos os testes foram validados com saídas esperadas e estão documentados na apresentação PDF.

---
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/status-final-green)
![License](https://img.shields.io/badge/license-MIT-blue)

