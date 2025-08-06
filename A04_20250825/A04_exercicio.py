
DESCONTO = 0.10
l_nome_produto = input('Digite o nome do produto: ')
l_valor_produto = float(input('Informe o valor unitario do produto: '))
l_quantidade = int(input('Digite a quantidade do produto: '))

l_valor_bruto = l_quantidade * l_valor_produto
l_desconto = (l_valor_bruto * DESCONTO)
l_valor_liquido = l_valor_bruto - l_desconto

print(f'Valor bruto do produto é R${l_valor_bruto:.2f}')
print(f'Valor do desconto do produto é R${l_desconto:.2f}')
print(f'Valor final do produto é R${l_valor_liquido:.2f}')



