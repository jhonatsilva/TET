DESCONTO = 0.10  
acervo = []

livros_vendidos = []

def cadastrar_livros():
    quantidade_livros = validar_inteiro("Quantos livros deseja cadastrar? ")
    for i in range(quantidade_livros):
        print(f"\nCadastro do livro {i + 1}:")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        preco = validar_float("Digite o preço do livro: ")
        ano_publicacao = validar_inteiro("Digite o ano de publicação do livro: ")
        quantidade = validar_inteiro("Digite a quantidade de livros: ")
        
        acervo.append({
            "titulo": titulo,
            "autor": autor,
            "preco": preco,
            "ano_publicacao": ano_publicacao,
            "quantidade": quantidade
        })

def validar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número decimal válido.")
            
def exibir_livros():
    if not acervo:
        print("\nNenhum livro cadastrado.")
    else:
        print("\nLivros cadastrados:")
        for i, livro in enumerate(acervo, start=1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Preço: R${livro['preco']:.2f}, "
                  f"Ano: {livro['ano_publicacao']}, Quantidade: {livro['quantidade']}")

def vender_livros():
    if not acervo:
        print("\nNenhum livro disponível para venda.")
        return

    exibir_livros()
    escolha = validar_inteiro("\nDigite o número do livro que deseja vender: ") - 1

    if 0 <= escolha < len(acervo):
        livro = acervo[escolha]
        quantidade_venda = validar_inteiro(f"Digite a quantidade de '{livro['titulo']}' que deseja vender: ")

        if quantidade_venda > livro["quantidade"]:
            print("Quantidade insuficiente em estoque!")
        else:
            valor_total = quantidade_venda * livro["preco"]
            valor_com_desconto = valor_total * (1 - DESCONTO)

            # Atualizando o estoque
            livro["quantidade"] -= quantidade_venda

            # Registrando a venda
            livros_vendidos.append({
                "titulo": livro["titulo"],
                "quantidade": quantidade_venda,
                "valor_total": valor_com_desconto
            })

            # Exibindo o valor da venda
            print(f"\nVenda realizada!")
            print(f"Quantidade vendida: {quantidade_venda}")
            print(f"Valor total sem desconto: R${valor_total:.2f}")
            print(f"Valor total com desconto: R${valor_com_desconto:.2f}")
            print(f"Estoque atualizado: {livro['quantidade']} unidades restantes.")
    else:
        print("Opção inválida.")

def exibir_vendas():
    if not livros_vendidos:
        print("\nNenhuma venda realizada.")
    else:
        print("\nLivros vendidos:")
        total_arrecadado = 0
        for i, venda in enumerate(livros_vendidos, start=1):
            print(f"{i}. Título: {venda['titulo']}, Quantidade: {venda['quantidade']}, "
                  f"Valor Total: R${venda['valor_total']:.2f}")
            total_arrecadado += venda["valor_total"]
        print(f"\nTotal arrecadado: R${total_arrecadado:.2f}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar livros")
        print("2. Exibir livros cadastrados")
        print("3. Vender livros")
        print("4. Exibir vendas realizadas")
        print("5. Sair")
        opcao = validar_inteiro("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_livros()
        elif opcao == 2:
            exibir_livros()
        elif opcao == 3:
            vender_livros()
        elif opcao == 4:
            exibir_vendas()
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()