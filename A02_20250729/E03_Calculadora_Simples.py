l_numero_1 = float(input("Digite o primeiro número: "))
l_numero_2 = float(input("Digite o segundo número: "))
l_soma = l_numero_1 + l_numero_2
l_subtracao = l_numero_1 - l_numero_2
l_multiplicacao = l_numero_1 * l_numero_2
l_divisao = l_numero_1 / l_numero_2 if l_numero_2 != 0 else "Divisão por zero não é permitida"

print(f"A soma é: {l_soma}")
print(f"A subtração é: {l_subtracao}")
print(f"A multiplicação é: {l_multiplicacao}")
print(f"A divisão é: {l_divisao}")  