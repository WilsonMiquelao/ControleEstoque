
lista_de_produtos = []


totalProdutos = 0

def adicionar_produto():
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade: "))
    valor_unitario = float(input("Informe o valor unitário: "))

    total_produto = quantidade * valor_unitario

    produto = {"produto": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total_produto}

    lista_de_produtos.append(produto)

    global totalProdutos
    totalProdutos += total_produto

def mostrar_lista_de_produtos():
    print("Lista de Produtos:")
    for produto in lista_de_produtos:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']}, Total: {produto['total']}")
    print(f"Total de todos os produtos: {totalProdutos}")

def atualizar_produto():
    nome = input("Informe o nome do produto que deseja atualizar: ")
    for produto in lista_de_produtos:
        if produto["produto"] == nome:
            quantidade = int(input("Informe a nova quantidade: "))
            valor_unitario = float(input("Informe o novo valor unitário: "))
            produto["quantidade"] = quantidade
            produto["valor"] = valor_unitario
            produto["total"] = quantidade * valor_unitario

            global totalProdutos
            totalProdutos = sum(produto["total"] for produto in lista_de_produtos)
            break
    else:
        print("Produto não encontrado!")

def remover_produto():
    nome = input("Informe o nome do produto que deseja remover: ")
    for produto in lista_de_produtos:
        if produto["produto"] == nome:
            lista_de_produtos.remove(produto)
            
            global totalProdutos
            totalProdutos = sum(produto["total"] for produto in lista_de_produtos)
            break
    else:
        print("Produto não encontrado!")

def main():
    while True:
        print("\nOpções:")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            mostrar_lista_de_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
