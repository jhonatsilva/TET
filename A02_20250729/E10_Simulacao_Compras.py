l_produtos = []
l_total = 0

for i in range(1, 4):
    l_nome = input(f"Digite o l_nome do produto {i}: ")
    l_preco = float(input(f"Digite o preço de {l_nome} (em R$): "))
    l_produtos.append((l_nome, l_preco))
    l_total += l_preco

l_desconto = 0
if l_total > 100:
    l_desconto = l_total * 0.10

l_valor_final = l_total - l_desconto

# Mostra os resultados
print("\nResumo da compra:")
for l_nome, l_preco in l_produtos:
    print(f"- {l_nome}: R$ {l_preco:.2f}")

print(f"\n total sem l_desconto: R$ {l_total:.2f}")
if l_desconto > 0:
    print(f"desconto aplicado: R$ {l_desconto:.2f}")
else:
    print("Nenhum desconto aplicado.")
print(f"Valor final a pagar: R$ {l_valor_final:.2f}")
