# Sistema de Controle de Produtos

Pequeno sistema em Python para controle de estoque de produtos com funcionalidades básicas de um CRUD (Create, Read, Update, Delete), executado via terminal.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto
- **CLI (Command Line Interface)**: Interface interativa via terminal
- **Estrutura procedural**: Códigos organizados por funções

---

## 📋 Funcionalidades

- ✅ Adicionar produto
- ✅ Visualizar todos os produtos cadastrados
- ✅ Atualizar quantidade e valor de um produto existente
- ✅ Remover produto da lista
- ✅ Cálculo automático do valor total do estoque

---

## 🧠 Lógica e Estrutura

### Variáveis principais

- `lista_de_produtos`: lista que armazena todos os produtos como dicionários
- `totalProdutos`: armazena o valor total acumulado de todos os produtos

### Funções

- `adicionar_produto()`: coleta dados do produto e adiciona à lista
- `mostrar_lista_de_produtos()`: exibe todos os produtos e o total geral
- `atualizar_produto()`: atualiza dados de um produto existente
- `remover_produto()`: exclui um produto da lista
- `main()`: exibe o menu e gerencia o fluxo da aplicação

### Exemplo de menu:

1- Adicionar produto
2- Ver lista de produtos
3- Atualizar produto
4- Remover produto
5- Encerrar programa
