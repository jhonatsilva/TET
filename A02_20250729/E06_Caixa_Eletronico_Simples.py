# Solicita o l_valor do saque
l_valor = int(input("Digite o l_valor do saque (múltiplo de 10): R$ "))

# Verifica se o l_valor é válido
if l_valor % 10 != 0 or l_valor <= 0:
    print("l_valor inválido. Por favor, digite um l_valor positivo e múltiplo de 10.")
else:
    l_cedulas_100 = l_valor // 100
    l_valor = l_valor % 100

    l_cedulas_50 = l_valor // 50
    l_valor = l_valor % 50

    l_cedulas_20 = l_valor // 20
    l_valor = l_valor % 20

    l_cedulas_10 = l_valor // 10

    # Exibe o resultado
    print("Cédulas fornecidas:")
    if l_cedulas_100 > 0:
        print(f"{l_cedulas_100} x R$100")
    if l_cedulas_50 > 0:
        print(f"{l_cedulas_50} x R$50")
    if l_cedulas_20 > 0:
        print(f"{l_cedulas_20} x R$20")
    if l_cedulas_10 > 0:
        print(f"{l_cedulas_10} x R$10")


