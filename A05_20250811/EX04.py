produtos = {}
ordem_cadastro = []

for i in range(3):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto {i + 1}: R$ "))
    produtos[nome] = preco
    ordem_cadastro.append(nome)

print("\nProdutos cadastrados:")
for nome in ordem_cadastro:
    preco = produtos[nome]
    print(f"{nome}: R$ {preco:.2f}")